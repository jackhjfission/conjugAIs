from pydantic import BaseModel


class Option(BaseModel):
    name: str
    instruction: str
    description: str


class Mode(BaseModel):
    name: str
    description: str
    options: list[Option]
    is_choice: bool


class Component(BaseModel):
    word_options: list[str]
    function: Option
    modes: list[Mode]
    optional: bool


class ClauseTemplate(BaseModel):
    name: str
    description: str
    language: str
    components: list[Component]
