import os
from core.schemas import FactValidation
from openai import OpenAI

def load_prompt(backstory: str, hidden_fact: str, user_fact: str) -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(backstory=backstory, hidden_fact=hidden_fact, user_fact=user_fact)

def check_fact(client: OpenAI, user_fact: str, backstory: str, hidden_fact: str) -> bool:
    prompt = load_prompt(backstory, hidden_fact, user_fact)
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": prompt},
        ],
        response_format=FactValidation,
    )
    return response.choices[0].message.parsed.is_correct