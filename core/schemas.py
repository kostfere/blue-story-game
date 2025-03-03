from pydantic import BaseModel, Field


class Mystery(BaseModel):
    title: str = Field(..., description="A title for the mystery.")
    backstory: str = Field(..., description="A short but engaging backstory.")
    answer: str = Field(..., description="A key fact that the player must deduce.")


class YesNoResponse(BaseModel):
    answer: str = Field(..., description="The answer must be 'Yes', 'No', or 'Irrelevant'.")


class FactValidation(BaseModel):
    result: str = Field(..., description="One of 'Yes', 'No', or 'Yes but incomplete'.")
