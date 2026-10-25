import express from 'express';
import cors from 'cors';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';
import mongoose from 'mongoose';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const DATA_DIR = path.join(__dirname, 'data');
const QUESTIONS_FILE = path.join(DATA_DIR, 'questions.json');
const LEADERBOARD_FILE = path.join(DATA_DIR, 'leaderboard.json');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5001;

// Ensure local data files exist
if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}
if (!fs.existsSync(LEADERBOARD_FILE)) {
  fs.writeFileSync(LEADERBOARD_FILE, JSON.stringify([
    { teamName: "NetGuardians", member1: "Alice", member2: "Bob", score: 850, levelReached: 5, timestamp: new Date() },
    { teamName: "ZeroTrusters", member1: "Charlie", member2: "David", score: 720, levelReached: 4, timestamp: new Date() },
    { teamName: "CyberSamurais", member1: "Eva", member2: "Frank", score: 640, levelReached: 4, timestamp: new Date() }
  ], null, 2));
}

// Database Connection Flag
let isMongoConnected = false;

// Define MongoDB Schemas if URI is present
const questionSchema = new mongoose.Schema({
  id: String,
  level: Number,
  topic: String,
  question: String,
  options: [String],
  answer: String
});

const leaderboardSchema = new mongoose.Schema({
  teamName: String,
  member1: String,
  member2: String,
  score: Number,
  levelReached: Number,
  timestamp: { type: Date, default: Date.now }
});

let MongoQuestion;
let MongoLeaderboard;

if (process.env.MONGODB_URI) {
  mongoose.connect(process.env.MONGODB_URI)
    .then(() => {
      console.log("Connected to MongoDB successfully!");
      isMongoConnected = true;
      MongoQuestion = mongoose.model('Question', questionSchema);
      MongoLeaderboard = mongoose.model('Leaderboard', leaderboardSchema);
      
      // Seed MongoDB with initial questions if empty
      MongoQuestion.countDocuments().then(count => {
        if (count === 0 && fs.existsSync(QUESTIONS_FILE)) {
          const localQuestions = JSON.parse(fs.readFileSync(QUESTIONS_FILE, 'utf-8'));
          MongoQuestion.insertMany(localQuestions)
            .then(() => console.log("Seeded MongoDB with local questions database."))
            .catch(err => console.error("Error seeding MongoDB:", err));
        }
      });
    })
    .catch(err => {
      console.error("MongoDB connection failed! Falling back to Local JSON Database:", err.message);
    });
} else {
  console.log("No MONGODB_URI found. Operating in Local JSON Database Mode.");
}

// Helper: Load questions
const getQuestions = async () => {
  if (isMongoConnected) {
    return await MongoQuestion.find({});
  } else {
    if (fs.existsSync(QUESTIONS_FILE)) {
      return JSON.parse(fs.readFileSync(QUESTIONS_FILE, 'utf-8'));
    }
    return [];
  }
};

// Helper: Save questions (for Admin changes)
const saveQuestions = async (questions) => {
  if (isMongoConnected) {
    // Drop existing and replace (or modify individually).
    // For admin simplicity in this setup, update individual or reload
    await MongoQuestion.deleteMany({});
    await MongoQuestion.insertMany(questions);
  } else {
    fs.writeFileSync(QUESTIONS_FILE, JSON.stringify(questions, null, 2), 'utf-8');
  }
};

// Helper: Load Leaderboard
const getLeaderboard = async () => {
  if (isMongoConnected) {
    return await MongoLeaderboard.find({}).sort({ score: -1 }).limit(10);
  } else {
    if (fs.existsSync(LEADERBOARD_FILE)) {
      const data = JSON.parse(fs.readFileSync(LEADERBOARD_FILE, 'utf-8'));
      return data.sort((a, b) => b.score - a.score).slice(0, 10);
    }
    return [];
  }
};

// Helper: Save Leaderboard entry (Upsert by teamName)
const addLeaderboardEntry = async (entry) => {
  if (isMongoConnected) {
    const existing = await MongoLeaderboard.findOne({ teamName: new RegExp(`^${entry.teamName}$`, 'i') });
    if (existing) {
      if (entry.score > existing.score) {
        existing.score = entry.score;
        existing.levelReached = entry.levelReached;
        existing.member1 = entry.member1;
        existing.member2 = entry.member2;
        existing.timestamp = new Date();
        await existing.save();
      }
      return existing;
    } else {
      const newEntry = new MongoLeaderboard(entry);
      await newEntry.save();
      return newEntry;
    }
  } else {
    const current = JSON.parse(fs.readFileSync(LEADERBOARD_FILE, 'utf-8'));
    const existingIdx = current.findIndex(e => e.teamName.toLowerCase() === entry.teamName.toLowerCase());
    if (existingIdx !== -1) {
      if (entry.score > current[existingIdx].score) {
        current[existingIdx] = { ...current[existingIdx], ...entry };
      }
    } else {
      current.push(entry);
    }
    current.sort((a, b) => b.score - a.score);
    fs.writeFileSync(LEADERBOARD_FILE, JSON.stringify(current, null, 2), 'utf-8');
    return entry;
  }
};

// API Endpoints

// 1. Get Questions (shuffled or grouped)
app.get('/api/questions', async (req, res) => {
  try {
    const qList = await getQuestions();
    res.json(qList);
  } catch (err) {
    res.status(500).json({ error: "Failed to retrieve questions", message: err.message });
  }
});

// 2. Add custom question (Admin)
app.post('/api/questions', async (req, res) => {
  try {
    const { level, topic, question, options, answer } = req.body;
    if (!level || !topic || !question || !options || !answer) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    const qList = await getQuestions();
    const newQ = {
      id: `q_custom_${Date.now()}`,
      level: parseInt(level),
      topic,
      question,
      options,
      answer
    };

    if (isMongoConnected) {
      const mongoQ = new MongoQuestion(newQ);
      await mongoQ.save();
    } else {
      qList.push(newQ);
      await saveQuestions(qList);
    }

    res.status(201).json(newQ);
  } catch (err) {
    res.status(500).json({ error: "Failed to add question", message: err.message });
  }
});

// 3. Edit question (Admin)
app.put('/api/questions/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { level, topic, question, options, answer } = req.body;

    if (isMongoConnected) {
      const updated = await MongoQuestion.findOneAndUpdate(
        { id: id },
        { level, topic, question, options, answer },
        { new: true }
      );
      if (!updated) return res.status(404).json({ error: "Question not found" });
      res.json(updated);
    } else {
      const qList = await getQuestions();
      const idx = qList.findIndex(q => q.id === id);
      if (idx === -1) return res.status(404).json({ error: "Question not found" });

      qList[idx] = { ...qList[idx], level: parseInt(level), topic, question, options, answer };
      await saveQuestions(qList);
      res.json(qList[idx]);
    }
  } catch (err) {
    res.status(500).json({ error: "Failed to update question", message: err.message });
  }
});

// 4. Delete question (Admin)
app.delete('/api/questions/:id', async (req, res) => {
  try {
    const { id } = req.params;
    if (isMongoConnected) {
      const deleted = await MongoQuestion.findOneAndDelete({ id: id });
      if (!deleted) return res.status(404).json({ error: "Question not found" });
      res.json({ success: true, message: "Question deleted successfully" });
    } else {
      const qList = await getQuestions();
      const filtered = qList.filter(q => q.id !== id);
      if (qList.length === filtered.length) {
        return res.status(404).json({ error: "Question not found" });
      }
      await saveQuestions(filtered);
      res.json({ success: true, message: "Question deleted successfully" });
    }
  } catch (err) {
    res.status(500).json({ error: "Failed to delete question", message: err.message });
  }
});

// 5. Get Leaderboard (Top 10)
app.get('/api/leaderboard', async (req, res) => {
  try {
    const scores = await getLeaderboard();
    res.json(scores);
  } catch (err) {
    res.status(500).json({ error: "Failed to retrieve leaderboard", message: err.message });
  }
});

// 6. Submit Score to Leaderboard
app.post('/api/leaderboard', async (req, res) => {
  try {
    const { teamName, member1, member2, score, levelReached } = req.body;
    if (!teamName || !member1 || !member2 || score === undefined || levelReached === undefined) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    const entry = {
      teamName,
      member1,
      member2,
      score: parseInt(score),
      levelReached: parseInt(levelReached),
      timestamp: new Date()
    };

    const saved = await addLeaderboardEntry(entry);
    res.status(201).json(saved);
  } catch (err) {
    res.status(500).json({ error: "Failed to save leaderboard score", message: err.message });
  }
});

// 7. Reset Leaderboard / Database (Admin)
app.post('/api/reset', async (req, res) => {
  try {
    const { type } = req.body; // 'leaderboard' or 'questions' or 'all'
    if (type === 'leaderboard' || type === 'all') {
      if (isMongoConnected) {
        await MongoLeaderboard.deleteMany({});
      } else {
        fs.writeFileSync(LEADERBOARD_FILE, JSON.stringify([], null, 2), 'utf-8');
      }
    }
    
    if (type === 'questions' || type === 'all') {
      // Re-generate default questions using shell script or reload from questions.json
      // For now, re-seed from generated backup if available
      if (fs.existsSync(QUESTIONS_FILE)) {
        const localQuestions = JSON.parse(fs.readFileSync(QUESTIONS_FILE, 'utf-8'));
        if (isMongoConnected) {
          await MongoQuestion.deleteMany({});
          await MongoQuestion.insertMany(localQuestions);
        } else {
          // No operation needed since it reads directly from questions.json, unless we want to reset manual changes
        }
      }
    }
    res.json({ success: true, message: `Successfully reset: ${type}` });
  } catch (err) {
    res.status(500).json({ error: "Reset failed", message: err.message });
  }
});

// 8. Server Health / Mode Check
app.get('/api/status', (req, res) => {
  res.json({
    status: "online",
    database: isMongoConnected ? "MongoDB" : "Local JSON File",
    port: PORT
  });
});

app.listen(PORT, () => {
  console.log(`CYBRVEXIS Express Server running on http://localhost:${PORT}`);
});
