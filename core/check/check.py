import os
import os
from core.schemas import FactValidation
from openai import OpenAI
from core.check.check_answer_prompt import CHECK_ANSWER_PROMPT_TEMPLATE  # Import the prompt template from prompt.py

def load_prompt(backstory: str, answer: str, user_fact: str) -> str:
    return CHECK_ANSWER_PROMPT_TEMPLATE.format(backstory=backstory, answer=answer, user_fact=user_fact)

def check_fact(client: OpenAI, user_fact: str, backstory: str, answer: str) -> bool:
    prompt = load_prompt(backstory, answer, user_fact)
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": prompt},
        ],
        response_format=FactValidation,
    )
    return response.choices[0].message.parsed.is_correct