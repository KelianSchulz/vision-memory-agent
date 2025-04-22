# 🧠 Vision Memory Agent – Architecture & Reflection Loop

---

## 1. Overview

The Vision Memory Agent is a self-correcting AI system that:

- Selects relevant images based on a semantic goal
- Uses CLIP to measure image-text similarity
- Reflects when it fails to find enough relevant results
- Adapts its goal using GPT-based natural language feedback
- Retries with new goals until success or termination

---

## 2. Motivation

Most AI systems fail silently.  
This agent is different: it **recognizes failure** and **responds linguistically**.  
By leveraging GPT to reframe its own search goals, the system develops a form of **semantic self-correction** —  
a step toward more human-like, reflective intelligence.

---

## 3. Dataset

Uses **CIFAR-10**, containing the following object classes:
- airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

---

## 4. Architecture

### 🔁 Reflection Loop

```text
        ┌────────────┐
        │ Start goal │
        └─────┬──────┘
              ↓
     ┌────────────────────┐
     │ Search relevant    │
     │ images with CLIP   │
     └──────┬─────────────┘
            ↓
  [success] ≥ required? ─────────┐
            │ no                │ yes
            ↓                   ↓
┌──────────────────────┐   ┌───────────────┐
│ Ask GPT for better   │   │ Save memory   │
│ goal (1 suggestion)  │   └───────────────┘
└─────┬────────────────┘
      ↓
  [retry up to 5 times]
```

---

## 5. Core Components

| Module               | Role                                                |
|----------------------|-----------------------------------------------------|
| `vision_agent.py`    | Main loop: search, evaluate, reflect                |
| `embedding.py`       | CLIP-based image and text encoding                  |
| `gpt_helpers.py`     | Handles GPT goal reformulation                      |
| `visualize_memory.py`| Displays final selected images and scores           |
| `agent_memory.json`  | Stores the final goal and matching image indices    |
| `goal_trace.json`    | Logs each goal attempt, hits, and origin            |

---

## 6. GPT Prompt (Reflection)

```text
Original: {original_goal}
Tried: {list of tested goals}
Suggest 1 short visual phrase (max 4 words) close in meaning.
Use CIFAR-10 terms. Avoid tried. No quotes. Just the phrase.
```

---

## 7. Future Work

- Multi-goal suggestion with scoring
- Visual reasoning feedback per match
- Goal path visualization and drift tracking
- Extension to other modalities (text, audio)
- Reuse of failed attempts in future sessions

---

## 8. Author

Designed and built by **Kelian Schulz**  
As part of an independent research journey toward  
**self-guided, reflective, human-aligned AI systems**.