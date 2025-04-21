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

# Ziel
goal = "a police car at night"
goal_vec = embed_text(goal, model, device)

# Dataset
transform = transforms.Compose([transforms.ToPILImage()])
dataset = CIFAR10(root="data/", download=True)
trys = 0
# Agentenlauf
agent_memory = []

while len(agent_memory) < 5 and trys < 5:
    print(f"\n🎯 Attempt {trys+1}/5 – Searching for goal: '{goal}'")
    goal_vec = embed_text(goal, model, device)
    agent_memory = []

    for i in range(1000):
        img, _ = dataset[i]
        image_vec = embed_image(img, model, preprocess, device)
        score = cosine_similarity(image_vec, goal_vec)

        if score > 0.29:
            agent_memory.append({"index": i, "score": float(score)})

        if i % 100 == 0:
            print(f"Checked image {i}/1000")

    if len(agent_memory) < 5:
        trys += 1
        print(f"\n⚠️ Too few matches for goal '{goal}' – asking GPT for a new goal...")
        alternatives = suggest_new_goals(goal)
        print("🔁 GPT suggestions:")
        for alt in alternatives:
            print("→", alt)
        new_goal = alternatives[0] if alternatives else None
        if not new_goal:
            print("❌ GPT failed to suggest a new goal. Stopping.")
            break
        goal = new_goal
    else:
        print(f"\n✅ Found {len(agent_memory)} relevant images for goal '{goal}'")

       
        with open("data/agent_memory.json", "w", encoding="utf-8") as f:
            json.dump({
                "goal": goal,
                "memory": agent_memory
            }, f, indent=4)

        break

if trys >= 5:
    print("\n🛑 Stopped: Too many failed attempts. Consider changing the starting goal.")