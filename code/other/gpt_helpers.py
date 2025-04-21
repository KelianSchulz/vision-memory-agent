from openai import OpenAI
import os
from dotenv import load_dotenv

# .env einlesen
load_dotenv()

# GPT-Client erzeugen
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_new_goals(failed_goal):
    prompt = f"""
        My goal '{failed_goal}' failed to retrieve relevant images using CLIP on the CIFAR-10 dataset.
        CIFAR-10 includes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.
        Give me a short, visually clear goal phrase related to these classes.
        """


    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content
    return [line.strip("- ").strip() for line in text.splitlines() if line.strip()]
