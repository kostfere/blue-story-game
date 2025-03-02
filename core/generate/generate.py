import os
from core.schemas import Mystery
from core.generate.generate_story_prompt import GENERATE_STORY_PROMPT
from openai import OpenAI

def generate_mystery(client: OpenAI) -> Mystery:
    prompt = GENERATE_STORY_PROMPT
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Create an intriguing lateral thinking mystery."},
        ],
        response_format=Mystery,
        temperature=1.4,
    )
    return response.choices[0].message.parsed