from pydantic import BaseModel


class Option(BaseModel):
    name: str
    instruction: str
    description: str
    language: str


class Mode(BaseModel):
    name: str
    description: str
    options: list[Option]
    is_choice: bool
