from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_new_goals(original_goal, already_tried=[]):
        tried_str = ", ".join(f'"{g}"' for g in already_tried)
        prompt = (
        f"Original: {original_goal}\n"
        f"Tried: {tried_str}\n"
        "Suggest 1 short visual phrase (max 4 words) close in meaning. "
        "Use CIFAR-10 terms. Avoid tried. No quotes. Just the phrase."
    )



        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        text = response.choices[0].message.content
        return [line.strip("-•* ").strip().strip('"') for line in text.splitlines() if line.strip()]

