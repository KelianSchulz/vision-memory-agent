import matplotlib.pyplot as plt
import json
from torchvision.datasets import CIFAR10


dataset = CIFAR10(root="data/", download=False)

with open("data/agent_memory.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    memory = data["memory"]
    goal = data["goal"]



n = min(len(memory), 10)

fig, axes = plt.subplots(1, n, figsize=(n*2, 2))
plt.suptitle(f"Goal: '{goal}'", fontsize=14)

for i in range(n):
    idx = memory[i]["index"]
    score = memory[i]["score"]
    img, _ = dataset[idx]

    axes[i].imshow(img)
    axes[i].set_title(f"{score:.2f}", fontsize=8)
    axes[i].axis("off")

plt.tight_layout()
plt.show()