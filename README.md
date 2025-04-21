# 🧠 Vision Memory Agent

A self-reflecting AI agent that selects and remembers images based on semantic similarity to a goal — and dynamically adjusts that goal using GPT when it fails.

---

## 🚀 What it does

- Uses OpenAI's CLIP to compare images from the CIFAR-10 dataset with a goal phrase (e.g. `"a cat in a red car"`)
- If the agent finds **too few relevant images**, it asks GPT for **better goal alternatives**
- Repeats the search with the new goal until it succeeds or exhausts its attempts
- Stores the **final goal** and **relevant image indices + scores** in `agent_memory.json`

---

## 🤖 How it works

1. Embed the goal phrase and CIFAR-10 images using CLIP
2. Compute cosine similarity for each image
3. If less than 5 matches are found:
   - Ask GPT: *"Suggest better goals for CIFAR-10"*
   - Use GPT's first suggestion as the new goal
   - Try again (up to 5 times)

---

## 🧪 Example Output

```
🎯 Attempt 1/5 – Searching for goal: 'a cat in a red car'
⚠️ Too few matches – asking GPT...

🔁 GPT suggestions:
→ "a tuxedo cat on a red sofa"
→ "a black dog playing on grass"
→ "a bird flying over a lake"

🎯 Attempt 2/5 – Searching for goal: 'a tuxedo cat on a red sofa'
✅ Found 6 relevant images.
```

---

## 📁 Files

- `vision_agent.py` – main agent loop
- `embedding.py` – helper functions for CLIP
- `gpt_helpers.py` – GPT-powered goal suggestions
- `visualize_memory.py` – visualize results
- `agent_memory.json` – stores results and final goal

---

## 🧠 Why it's interesting

This project explores **semantic self-correction** in agents:
- Can a visual agent notice its own failure?
- Can it adjust goals using language?
- Can it learn to "try better"?

---

## 📄 See also

👉 [`agent_architecture.md`](agent_architecture.md) – for full explanation of system design & reasoning loop.


## ✍️ Author

Built by Kelian Schulz – as part of a deeper exploration into  
interpretable, goal-driven agents for applied AI research.
