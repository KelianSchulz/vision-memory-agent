# 🧠 Vision Memory Agent – Architecture & Reflection Loop

---

## 1. Overview

The Vision Memory Agent is an AI system that:

- Selects relevant images based on a semantic goal
- Builds a memory of relevant items
- Reflects when it fails
- Adapts its goal through natural language
- Tries again until it succeeds or gives up

---

## 2. Motivation

In most AI systems, failure is silent.  
This agent **notices** when it fails and **responds** by adjusting its internal goal.  
It uses **language (GPT)** to reinterpret its objective and tries again, making it more human-like in how it learns.

---

## 3. Dataset

Uses **CIFAR-10** (10 object classes):
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
  [success] ≥ 5 results? ─────────┐
            │ no                 │ yes
            ↓                    ↓
┌──────────────────────┐   ┌───────────────┐
│ Ask GPT for better   │   │ Save memory   │
│ goal alternatives    │   └───────────────┘
└─────┬────────────────┘
      ↓
  [retry up to 5 times]
```

---

## 5. Core Components

| Module             | Role                                                |
|--------------------|-----------------------------------------------------|
| `vision_agent.py`  | Main loop: search, evaluate, reflect                |
| `embedding.py`     | CLIP-based image and text encoding                  |
| `gpt_helpers.py`   | Handles GPT goal reformulation                      |
| `visualize_memory.py` | Displays final selected images and scores        |
| `agent_memory.json`| Stores goal + final selection                       |

---

## 6. GPT Prompt (Reflection)

```text
My goal '{failed_goal}' failed to retrieve relevant images using CLIP on the CIFAR-10 dataset.
CIFAR-10 includes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.
Give me 3 short, visually clear goal phrases related to these classes.
```

---

## 7. Future Work

- Multi-goal reasoning (choose best of 3)
- Score-based memory explanation
- Visual-semantic drift tracking
- Reflexive agents in language and text

---

## 8. Author

Designed and built by **Kelian Schulz**  
As part of an independent research path exploring  
**self-guided, reflective AI systems**.
