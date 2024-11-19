from pydantic import BaseModel

class UserInput(BaseModel):
    name: str


class LLMInput(BaseModel):
    ticker: str
    metrics : str