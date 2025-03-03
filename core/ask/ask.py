from openai import OpenAI

from core.ask.answer_question_prompt import ANSWER_QUESTION_PROMPT_TEMPLATE
from core.schemas import Mystery, YesNoResponse


def load_prompt(backstory: str, answer: str) -> str:
    return ANSWER_QUESTION_PROMPT_TEMPLATE.format(backstory=backstory, answer=answer)


def ask_question(client: OpenAI, user_question: str, mystery: Mystery) -> str:
    prompt = load_prompt(mystery.backstory, mystery.answer)
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_question},
        ],
        response_format=YesNoResponse,
    )
    return response.choices[0].message.parsed.answer
