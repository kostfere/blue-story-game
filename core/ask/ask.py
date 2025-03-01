import os
from core.schemas import YesNoResponse
from openai import OpenAI

def load_prompt(backstory: str, hidden_fact: str) -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(backstory=backstory, hidden_fact=hidden_fact)

def ask_question(client: OpenAI, user_question: str, backstory: str, hidden_fact: str) -> str:
    prompt = load_prompt(backstory, hidden_fact)
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_question},
        ],
        response_format=YesNoResponse,
    )
    return response.choices[0].message.parsed.answer