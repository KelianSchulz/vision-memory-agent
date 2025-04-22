from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_new_goals(failed_goal):
    prompt = f"""
        Failed to find images for: "{failed_goal}" using CLIP on CIFAR-10.
        Give < short, direct goal phrase likely to match CIFAR-10 classes:
        airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.
        No quotes, no explanation.
        """


    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content
    return [line.strip("- ").strip() for line in text.splitlines() if line.strip()]
