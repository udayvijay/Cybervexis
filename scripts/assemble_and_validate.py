# -*- coding: utf-8 -*-
"""
Assembler & Validator for CyberVexis Questions.
Combines 250 new School questions with 375 untouched University questions.
"""
import json
import os
import sys

from level1 import level1_questions
from level2 import level2_questions
from level3 import level3_questions
from level4 import level4_questions
from level5 import level5_questions

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    questions_json_path = os.path.join(base_dir, 'server', 'data', 'questions.json')
    questions_js_path = os.path.join(base_dir, 'client', 'src', 'utils', 'questions.js')

    # 1. Combine new School questions
    new_school_questions = (
        level1_questions +
        level2_questions +
        level3_questions +
        level4_questions +
        level5_questions
    )

    print(f"Total new School questions: {len(new_school_questions)}")
    assert len(new_school_questions) == 250, f"Expected 250 School questions, got {len(new_school_questions)}"

    # 2. Validate each question
    expected_board_tiles = {
        1: [
            "Weak Password Attack",
            "Phishing Attack",
            "Malware Infection",
            "Unsafe Public Wi-Fi",
            "Data Leak"
        ],
        2: [
            "Packet Filtering Firewall",
            "Stateful Inspection Firewall",
            "Proxy Firewall (Application-Level Gateway)",
            "Cloud Firewall",
            "Software Firewall"
        ],
        3: [
            "In-House SOC",
            "Managed SOC",
            "Hybrid SOC",
            "Co-Managed SOC",
            "Virtual SOC (vSOC)"
        ],
        4: [
            "Identity-Based Architecture",
            "Device-Based Architecture",
            "Network-Based Architecture",
            "Data-Centric Architecture",
            "Infrastructure-Based Architecture"
        ],
        5: [
            "Preventive Resilience",
            "Detective Resilience",
            "Responsive Resilience",
            "Recovery Resilience",
            "Adaptive (Evolving) Resilience"
        ]
    }

    seen_ids = set()
    topic_counts = {}

    for idx, q in enumerate(new_school_questions):
        qid = q.get('id')
        assert qid, f"Question at index {idx} has no id"
        assert qid not in seen_ids, f"Duplicate id: {qid}"
        seen_ids.add(qid)

        assert q.get('mode') == 'school', f"{qid}: mode must be 'school'"
        lvl = q.get('level')
        assert lvl in [1, 2, 3, 4, 5], f"{qid}: invalid level {lvl}"

        topic = q.get('topic')
        assert topic in expected_board_tiles[lvl], f"{qid}: unexpected topic '{topic}' for level {lvl}"

        topic_counts[topic] = topic_counts.get(topic, 0) + 1

        # Check options
        opts_en = q.get('options_en')
        opts_hi = q.get('options_hi')
        assert isinstance(opts_en, list) and len(opts_en) == 4, f"{qid}: options_en must have 4 items"
        assert isinstance(opts_hi, list) and len(opts_hi) == 4, f"{qid}: options_hi must have 4 items"

        for opt in opts_en:
            assert isinstance(opt, str) and len(opt.strip()) > 0, f"{qid}: empty English option"
        for opt in opts_hi:
            assert isinstance(opt, str) and len(opt.strip()) > 0, f"{qid}: empty Hindi option"

        # Check correctAnswerIndex & answer
        c_idx = q.get('correctAnswerIndex')
        assert c_idx in [0, 1, 2, 3], f"{qid}: invalid correctAnswerIndex {c_idx}"
        ans = q.get('answer')
        assert ans == opts_en[c_idx], f"{qid}: answer '{ans}' does not match options_en[{c_idx}] ('{opts_en[c_idx]}')"

        # Check sync between options and options_en, question and question_en
        assert q.get('options') == opts_en, f"{qid}: options != options_en"
        assert q.get('question') == q.get('question_en'), f"{qid}: question != question_en"

        # Normalize explanation and explanation_en
        if q.get('explanation'):
            q['explanation_en'] = q['explanation']
        elif q.get('explanation_en'):
            q['explanation'] = q['explanation_en']

        # Check explanations
        assert q.get('explanation_en') and len(q.get('explanation_en').strip()) > 0, f"{qid}: missing explanation_en"
        assert q.get('explanation_hi') and len(q.get('explanation_hi').strip()) > 0, f"{qid}: missing explanation_hi"
        assert q.get('explanation') == q.get('explanation_en'), f"{qid}: explanation != explanation_en"

    # Verify each of the 25 topics has exactly 10 questions
    print("\nVerifying 25 topics count (10 each):")
    for lvl in range(1, 6):
        for top in expected_board_tiles[lvl]:
            cnt = topic_counts.get(top, 0)
            print(f"  Level {lvl} | {top}: {cnt} questions")
            assert cnt == 10, f"Topic '{top}' has {cnt} questions, expected 10!"

    print("\nAll 250 new School questions successfully passed all validation checks!")

    # 3. Read existing questions and isolate University questions
    with open(questions_json_path, 'r', encoding='utf-8') as f:
        existing_questions = json.load(f)

    original_uni = [q for q in existing_questions if q.get('mode') == 'university']
    original_school = [q for q in existing_questions if q.get('mode') == 'school']

    print(f"\nOriginal questions in {questions_json_path}:")
    print(f"  School: {len(original_school)}")
    print(f"  University: {len(original_uni)}")
    assert len(original_uni) == 375, f"Expected 375 original University questions, got {len(original_uni)}"

    # 4. Assemble the combined database:
    # We will order by Level 1 to 5, interleaved or level-by-level (School then University, or all School then all University)
    # Keeping the original convention: Level-by-level, school questions then university questions per level.
    # Let's inspect the original ordering:
    combined_questions = []
    for lvl in range(1, 6):
        lvl_school = [q for q in new_school_questions if q['level'] == lvl]
        lvl_uni = [q for q in original_uni if q['level'] == lvl]
        combined_questions.extend(lvl_school)
        combined_questions.extend(lvl_uni)

    print(f"\nTotal combined questions: {len(combined_questions)} (250 School + 375 University)")
    assert len(combined_questions) == 625

    # 5. Verify University questions are 100% UNTOUCHED
    combined_uni = [q for q in combined_questions if q.get('mode') == 'university']
    assert len(combined_uni) == len(original_uni), "University questions count changed!"
    for orig_q, new_q in zip(original_uni, combined_uni):
        assert orig_q == new_q, f"University question {orig_q.get('id')} was modified!"
    print("University questions verified: 100% untouched and identical!")

    # 6. Write to server/data/questions.json
    with open(questions_json_path, 'w', encoding='utf-8') as f:
        json.dump(combined_questions, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {questions_json_path}")

    # 7. Write to client/src/utils/questions.js
    js_content = (
        "// CYBERVEXIS Authoritative Question Database (625 Unique Questions)\n"
        "// 25 Topics x 10 School Questions (250) + 15 University Questions (375)\n"
        "// Supports English and Hindi translations\n\n"
        "export const questionBank = " + json.dumps(combined_questions, ensure_ascii=False, indent=2) + ";\n\n"
        "export function generateQuestionsLocally() {\n"
        "  return questionBank;\n"
        "}\n\n"
        "export default questionBank;\n"
    )

    with open(questions_js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"Successfully wrote {questions_js_path}")

if __name__ == '__main__':
    main()
