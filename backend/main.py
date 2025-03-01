from fastapi import FastAPI, HTTPException
from core.game import generate_mystery, ask_question, check_fact
from core.schemas import Mystery, YesNoResponse, FactValidation
import logging

app = FastAPI()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Global storage for the current mystery (for demonstration purposes)
current_mystery: Mystery = None

@app.post("/generate_mystery/", response_model=Mystery)
async def generate():
    global current_mystery
    try:
        current_mystery = generate_mystery()
        return current_mystery
    except Exception as e:
        logger.error("Error generating mystery: %s", e)
        raise HTTPException(status_code=500, detail="Error generating mystery")

@app.post("/ask_question/", response_model=YesNoResponse)
async def ask(user_question: str):
    if current_mystery is None:
        raise HTTPException(status_code=400, detail="No mystery has been generated yet.")
    try:
        answer = ask_question(user_question, current_mystery)
        return {"answer": answer}
    except Exception as e:
        logger.error("Error answering question: %s", e)
        raise HTTPException(status_code=500, detail="Error processing question")

@app.post("/check_fact/", response_model=FactValidation)
async def check(user_fact: str):
    if current_mystery is None:
        raise HTTPException(status_code=400, detail="No mystery has been generated yet.")
    try:
        is_correct = check_fact(user_fact, current_mystery)
        return {"is_correct": is_correct}
    except Exception as e:
        logger.error("Error checking fact: %s", e)
        raise HTTPException(status_code=500, detail="Error checking fact")