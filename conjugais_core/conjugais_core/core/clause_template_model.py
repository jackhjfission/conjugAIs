from pydantic import BaseModel


class ModeOption(BaseModel):
    name: str
    instruction: str
    description: str


class Mode(BaseModel):
    name: str
    description: str
    options: list[ModeOption]
    is_choice: bool


class WordFunction(BaseModel):
    name: str
    description: str


class Component(BaseModel):
    word_options: list[str]
    word_function: WordFunction
    modes: list[Mode]
    optional: bool


class ClauseTemplate(BaseModel):
    name: str
    description: str
    language: str
    components: list[Component]
