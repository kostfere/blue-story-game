from openai import OpenAI

from core.ask.ask import ask_question as ask_question_impl
from core.check.check import check_fact as check_fact_impl
from core.generate.generate import generate_mystery as generate_mystery_impl
from core.schemas import Mystery


def generate_mystery(client: OpenAI) -> Mystery:
    return generate_mystery_impl(client)


def ask_question(client: OpenAI, user_question: str, mystery: Mystery) -> str:
    return ask_question_impl(client, user_question, mystery.backstory, mystery.answer)


def check_fact(client: OpenAI, user_fact: str, mystery: Mystery) -> bool:
    return check_fact_impl(client, user_fact, mystery.backstory, mystery.answer)
