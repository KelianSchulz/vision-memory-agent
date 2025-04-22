# 🧠 Vision Memory Agent

A self-reflecting AI agent that selects and remembers images based on semantic similarity to a goal — and dynamically adjusts that goal using GPT when it fails.

---

## 🚀 What it does

- Uses OpenAI's CLIP to compare images from the CIFAR-10 dataset with a goal phrase (e.g. `"a cat in a red car"`)
- If the agent finds **too few relevant images**, it asks GPT for **1 refined alternative**
- Repeats the search with the new goal until it succeeds or hits 5 attempts
- Stores the **final goal** and **relevant image indices + scores** in `agent_memory.json`

---

## 🤖 How it works

1. Embed the goal phrase and CIFAR-10 images using CLIP
2. Compute cosine similarity for each image
3. If not enough matches are found:
   - Ask GPT: *"Suggest 1 short alternative close to original, avoiding tested ones"*
   - Try again with the new suggestion

---

## 🧪 Example Output

```
🎯 Attempt 1/5 – Searching for goal: 'a fire truck in the rain'
⚠️ Too few matches – asking GPT...

🔁 GPT suggestion:
→ rainy fire engine

🎯 Attempt 2/5 – Searching for goal: 'rainy fire engine'
✅ Found 11 relevant images.
```

---

## 📁 Files

- `vision_agent.py` – main agent loop
- `embedding.py` – helper functions for CLIP
- `gpt_helpers.py` – GPT-powered goal suggestions
- `visualize_memory.py` – visualize results
- `agent_memory.json` – stores successful goal and matches
- `goal_trace.json` – logs every attempt with hit stats

---

## 🧠 Why it's interesting

This project explores **semantic self-correction** in agents:
- Can a visual agent recognize its own failure?
- Can it reformulate its goal using language?
- Can it learn to improve search through meaning, not just code?

---

## 📄 See also

👉 [`agent_architecture.md`](agent_architecture.md) – for full explanation of the reflection loop and system components.

---

## ✍️ Author

Built by **Kelian Schulz** – as part of an independent research journey into  
interpretable, reflective, and goal-driven AI agents.