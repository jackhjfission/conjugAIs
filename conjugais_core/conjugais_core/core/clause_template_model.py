from pydantic import BaseModel


class Option(BaseModel):
    name: str
    instruction: str
    description: str
    language: str
