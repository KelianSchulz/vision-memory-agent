# 🧠 Vision Memory Agent

A lightweight semantic image selection agent that learns to **remember only the most relevant images** for a given textual goal – and **explains why**.

---

## 🎯 Project Goal

This project aims to build a vision-based learning agent that:
- Receives a **semantic goal** (e.g. "Space Exploration", "Urban Life")
- Reviews a set of images
- Selects only those **visually aligned** with the goal
- Justifies its decisions with **semantic keywords** (e.g. "astronaut", "rocket")

---

## 🧠 Core Idea

Powered by [CLIP](https://openai.com/research/clip), the agent maps **text and image** into the same vector space.  
This allows the agent to measure semantic similarity between:
- a **goal string**
- and each **image's content**

Then it:
- selects the most relevant images
- stores them as its **visual memory**
- and explains *why* they were selected

---

## 🧱 Planned Architecture

```text
goal: "Space Exploration"
        ↓
image folder ─────► embed each image
        ↓
embed goal text
        ↓
cosine similarity (goal ↔ image)
        ↓
select top images (above threshold)
        ↓
generate explanation
        ↓
store result in memory.json
```

---

## 📦 Project Structure (planned)

```
vision-memory-agent/
├── data/                  # images + memory files
├── code/                   # model logic (embed, select, explain)
├── main.py                # agent entry point
├── requirements.txt
├── README.md              # this file
└── vision_architecture.md # detailed technical design
```

---

## 🔮 Future Directions

- Use image captioning models to improve explanation
- Incorporate attention heatmaps for visual justification
- Extend to multi-modal memory: combine text + image selection
- Eventually: let agent select its **own visual learning goal**

---

## ✍️ Author

Built by Kelian Schulz – as part of a deeper exploration into  
interpretable, goal-driven agents for applied AI research.
