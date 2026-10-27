# -*- coding: utf-8 -*-
"""Apply concise, length-balanced answers and shuffle options.

The original question bank had two strong tells:
  * the correct answer was almost always option A (index 0)
  * the correct answer was almost always by far the longest option

This module applies hand-written concise answers (English + Hindi), puts the
original long answer into the explanation so no detail is lost, and shuffles
the options so the correct index is evenly distributed.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_JSON = ROOT / "server" / "data" / "questions.json"
QUESTIONS_JS = ROOT / "client" / "src" / "utils" / "questions.js"
OVERRIDES_JSON = ROOT / "scripts" / "answer_overrides.json"

SEED = 20261027


def load_overrides(path: Path = OVERRIDES_JSON) -> dict:
    if not path.exists():
        print(f"Warning: overrides file not found at {path}; only shuffling.")
        return {}
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError("answer overrides must be a JSON object")
    return data


def _append_detail(question: dict, old_en: str, old_hi: str) -> None:
    """Keep the full original answer visible in the feedback explanation."""
    explanation_en = question.get("explanation_en") or question.get("explanation") or ""
    if old_en and old_en not in explanation_en:
        explanation_en = f"Full answer: {old_en}. {explanation_en}".strip()
        question["explanation_en"] = explanation_en
        question["explanation"] = explanation_en

    explanation_hi = question.get("explanation_hi") or ""
    if old_hi and old_hi not in explanation_hi:
        explanation_hi = f"पूरा उत्तर: {old_hi}। {explanation_hi}".strip()
        question["explanation_hi"] = explanation_hi


def _permute(question: dict, desired_index: int, rng: random.Random) -> None:
    ci = question["correctAnswerIndex"]
    remaining_sources = [i for i in range(4) if i != ci]
    remaining_slots = [i for i in range(4) if i != desired_index]
    rng.shuffle(remaining_sources)

    permutation = [None] * 4
    permutation[desired_index] = ci
    for slot, source in zip(remaining_slots, remaining_sources):
        permutation[slot] = source

    question["options_en"] = [question["options_en"][src] for src in permutation]
    question["options_hi"] = [question["options_hi"][src] for src in permutation]
    question["options"] = question["options_en"]
    question["correctAnswerIndex"] = desired_index
    question["answer"] = question["options_en"][desired_index]


def rebalance_questions(questions: list[dict], overrides: dict, seed: int = SEED) -> list[dict]:
    rng = random.Random(seed)

    # Only touch questions that have not been through this migration yet.
    pending = [q for q in questions if not q.get("answerBalanced")]
    if not pending:
        return questions

    # Build an evenly distributed list of target positions.
    desired_indices = [i % 4 for i in range(len(pending))]
    rng.shuffle(desired_indices)

    missing = []
    for question, desired_index in zip(pending, desired_indices):
        qid = question["id"]
        ci = question["correctAnswerIndex"]
        override = overrides.get(qid, {})

        old_en = question["options_en"][ci]
        old_hi = question["options_hi"][ci]
        new_en = override.get("en")
        new_hi = override.get("hi")

        if new_en:
            if new_en in [o for i, o in enumerate(question["options_en"]) if i != ci]:
                raise ValueError(f"{qid}: new English answer duplicates a distractor")
            question["options_en"][ci] = new_en
        if new_hi:
            if new_hi in [o for i, o in enumerate(question["options_hi"]) if i != ci]:
                raise ValueError(f"{qid}: new Hindi answer duplicates a distractor")
            question["options_hi"][ci] = new_hi
        if new_en is None and new_hi is None and not override:
            missing.append(qid)

        if (new_en and new_en != old_en) or (new_hi and new_hi != old_hi):
            _append_detail(question, old_en, old_hi)

        question["options"] = question["options_en"]
        question["answer"] = question["options_en"][ci]
        _permute(question, desired_index, rng)
        question["answerBalanced"] = True

    if missing:
        print(f"Note: {len(missing)} question(s) had no override and were only shuffled.")
    return questions


def validate(questions: list[dict]) -> None:
    n = len(questions)
    assert n == 625, f"expected 625 questions, found {n}"

    index_counts = [0, 0, 0, 0]
    rank_counts_en = [0, 0, 0, 0]
    rank_counts_hi = [0, 0, 0, 0]
    unique_longest_en = 0
    unique_shortest_en = 0

    for q in questions:
        qid = q.get("id", "<missing>")
        ci = q.get("correctAnswerIndex")
        assert ci in (0, 1, 2, 3), f"{qid}: invalid correctAnswerIndex {ci}"
        assert len(q["options_en"]) == 4, f"{qid}: expected 4 English options"
        assert len(q["options_hi"]) == 4, f"{qid}: expected 4 Hindi options"
        assert q["options"] == q["options_en"], f"{qid}: options != options_en"
        assert q["answer"] == q["options_en"][ci], f"{qid}: answer mismatch"
        assert q.get("question") == q.get("question_en"), f"{qid}: question != question_en"
        assert q.get("explanation") == q.get("explanation_en"), f"{qid}: explanation != explanation_en"
        if q.get("answerBalanced"):
            assert q.get("explanation_en"), f"{qid}: missing explanation_en"
            assert q.get("explanation_hi"), f"{qid}: missing explanation_hi"

        for lang, key in (("en", "options_en"), ("hi", "options_hi")):
            options = q[key]
            assert all(isinstance(o, str) and o.strip() for o in options), f"{qid}: empty {lang} option"
            assert len(set(options)) == 4, f"{qid}: duplicate {lang} options"
            lengths = [len(o) for o in options]
            correct_len = lengths[ci]
            rank = sum(1 for length in lengths if length < correct_len)
            if lang == "en":
                rank_counts_en[rank] += 1
                if correct_len == max(lengths) and lengths.count(correct_len) == 1:
                    unique_longest_en += 1
                if correct_len == min(lengths) and lengths.count(correct_len) == 1:
                    unique_shortest_en += 1
            else:
                rank_counts_hi[rank] += 1
        index_counts[ci] += 1

    quarter = n / 4
    for label, counts in (
        ("correct index", index_counts),
        ("English length rank", rank_counts_en),
        ("Hindi length rank", rank_counts_hi),
    ):
        assert all(abs(c - quarter) <= n * 0.08 for c in counts), (
            f"{label} distribution is too skewed: {counts}"
        )
    assert unique_longest_en <= n * 0.35, (
        f"correct answer is uniquely longest too often: {unique_longest_en}/{n}"
    )
    assert unique_shortest_en <= n * 0.35, (
        f"correct answer is uniquely shortest too often: {unique_shortest_en}/{n}"
    )

    print(f"Validated {n} questions")
    print(f"  correct index counts:       {index_counts}")
    print(f"  English length rank counts: {rank_counts_en}")
    print(f"  Hindi length rank counts:   {rank_counts_hi}")
    print(f"  uniquely longest correct:   {unique_longest_en} ({unique_longest_en / n:.1%})")
    print(f"  uniquely shortest correct:  {unique_shortest_en} ({unique_shortest_en / n:.1%})")


def write_questions_js(questions: list[dict], path: Path = QUESTIONS_JS) -> None:
    js_content = (
        "// CYBERVEXIS Authoritative Question Database (625 Unique Questions)\n"
        "// 25 Topics x 10 School Questions (250) + 15 University Questions (375)\n"
        "// Supports English and Hindi translations\n\n"
        "export const questionBank = "
        + json.dumps(questions, ensure_ascii=False, indent=2)
        + ";\n\n"
        "export function generateQuestionsLocally() {\n"
        "  return questionBank;\n"
        "}\n\n"
        "export default questionBank;\n"
    )
    path.write_text(js_content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    parser.add_argument("--overrides", type=Path, default=OVERRIDES_JSON)
    args = parser.parse_args()

    questions = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    overrides = load_overrides(args.overrides)
    questions = rebalance_questions(questions, overrides)
    validate(questions)

    if args.check:
        return

    QUESTIONS_JSON.write_text(
        json.dumps(questions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    write_questions_js(questions)
    print(f"Wrote {QUESTIONS_JSON}")
    print(f"Wrote {QUESTIONS_JS}")


if __name__ == "__main__":
    main()
