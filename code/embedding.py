import torch
import numpy as np
import clip

def embed_image(img, model, preprocess, device):
    image_input = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        image_vec = model.encode_image(image_input)
    return image_vec[0].cpu().numpy()

def embed_text(text, model, device):
    tokens = clip.tokenize([text]).to(device)
    with torch.no_grad():
        text_vec = model.encode_text(tokens)
    return text_vec[0].cpu().numpy()

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
