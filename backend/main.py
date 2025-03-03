import logging

from fastapi import Depends, FastAPI, HTTPException
from openai import OpenAI

from core.game import ask_question, check_fact, generate_mystery
from core.schemas import FactValidation, Mystery, YesNoResponse

app = FastAPI()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

current_mystery: Mystery = None


def get_openai_client():
    return OpenAI()


@app.post("/generate_mystery/", response_model=Mystery)
async def generate(client: OpenAI = Depends(get_openai_client)):
    global current_mystery
    try:
        current_mystery = generate_mystery(client)
        return current_mystery
    except Exception as e:
        logger.error("Error generating mystery: %s", e)
        raise HTTPException(status_code=500, detail="Error generating mystery") from e


@app.post("/ask_question/", response_model=YesNoResponse)
async def ask(user_question: str, client: OpenAI = Depends(get_openai_client)):
    if current_mystery is None:
        raise HTTPException(status_code=400, detail="No mystery has been generated yet.")
    try:
        answer = ask_question(client, user_question, current_mystery)
        return {"answer": answer}
    except Exception as e:
        logger.error("Error answering question: %s", e)
        raise HTTPException(status_code=500, detail="Error processing question") from e


@app.post("/check_fact/", response_model=FactValidation)
async def check(user_fact: str, client: OpenAI = Depends(get_openai_client)):
    if current_mystery is None:
        raise HTTPException(status_code=400, detail="No mystery has been generated yet.")
    try:
        is_correct = check_fact(client, user_fact, current_mystery)
        return {"is_correct": is_correct}
    except Exception as e:
        logger.error("Error checking fact: %s", e)
        raise HTTPException(status_code=500, detail="Error checking fact") from e
