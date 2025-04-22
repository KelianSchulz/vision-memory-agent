from embedding import embed_image, embed_text, cosine_similarity
import clip
import torch
import json
from torchvision.datasets import CIFAR10
from torchvision import transforms
from other.gpt_helpers import suggest_new_goals 
# Setup
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32")
model = model.to(device)

tested_goals = set()
goal = "a fire truck in the rain"
goal_vec = embed_text(goal, model, device)
tested_goals.add(goal.strip().lower())

# Dataset
transform = transforms.Compose([transforms.ToPILImage()])
dataset = CIFAR10(root="data/", download=True)
trys = 0

agent_memory = []
log = []
original_goal = goal
log_type = "original"
required_hits = 5

while len(agent_memory) < required_hits and trys < 5:
    print(f"\n🎯 Attempt {trys+1}/5 – Searching for goal: '{goal}'")
    goal_vec = embed_text(goal, model, device)
    agent_memory = []
    
    for i in range(5000):
        img, _ = dataset[i]
        image_vec = embed_image(img, model, preprocess, device)
        score = cosine_similarity(image_vec, goal_vec)

        if score > 0.28:
            agent_memory.append({"index": i, "score": float(score)})

        if i % 100 == 0:
            print(f"Checked image {i}/5000")
    if agent_memory:
        avg_score = sum(e["score"] for e in agent_memory) / len(agent_memory)
    else:
        avg_score =  0.0

    log_entry = {
    "goal": goal,
    "n_hits": len(agent_memory),
    "avg_score": round(avg_score, 3),
    "comment": "",  # ← optional
    "source" : log_type 
    }             
    log.append(log_entry)   

    if len(agent_memory) < required_hits:
        trys += 1
        
        if trys >= 5:
            print("\n🛑 Stopped: Too many failed attempts. Consider changing the starting goal.")
            break
        print(f"\n⚠️ Too few matches for goal '{goal}' – asking GPT for a new goal...")
        alternatives = suggest_new_goals(original_goal, list(tested_goals))
        print("🔁 GPT suggestions:")
        for alt in alternatives:
            print("→", alt)
        new_goal = None
        for alt in alternatives:
            clean_alt = alt.strip().lower()
            if clean_alt in tested_goals:
                print(f"⛔ Already tested: {alt}")
                continue
            tested_goals.add(clean_alt)
            new_goal = alt
            break

        if not new_goal:
            print("❌ All GPT suggestions already tested. Stopping.")
            break

        goal = new_goal
        log_type = "gpt"


    else:
        print(f"\n✅ Found {len(agent_memory)} relevant images for goal '{goal}'")

       
        with open("data/agent_memory.json", "w", encoding="utf-8") as f:
            json.dump({
                "goal": goal,
                "memory": agent_memory
            }, f, indent=4)

        break



with open("data/goal_trace.json", "w", encoding="utf-8") as f:
    json.dump(log, f, indent=4)
