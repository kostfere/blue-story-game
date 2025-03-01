import os
from core.schemas import Mystery
from openai import OpenAI

def load_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_mystery(client: OpenAI) -> Mystery:
    prompt = load_prompt()
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Create an intriguing lateral thinking mystery."},
        ],
        response_format=Mystery,
    )
    return response.choices[0].message.parsed