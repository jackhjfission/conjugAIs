from textwrap import dedent

from pydantic import BaseModel


class ModeOption(BaseModel):
    name: str
    instruction: str
    description: str

    def to_llm_text(self) -> str:
        ...


class Mode(BaseModel):
    name: str
    description: str
    options: list[ModeOption]
    is_choice: bool

    def to_llm_text(self) -> str:
        ...


class WordFunction(BaseModel):
    name: str
    description: str


class Component(BaseModel):
    word_options: list[str]
    word_function: WordFunction
    modes: list[Mode]
    optional: bool
    word_count: Mode

    def to_llm_text(self) -> str:
        return (
            f"* Choose one or more words for this sentence with the function: {self.word_function.name} "
            f"  from the selection {self.word_options}. "
            f"* If the word selection is empty, choose words yourself. "
            f"* The inclusion of this word function is {'optional' if self.optional else 'mandatory'} in this sentence."
            f"* If a word of this function is included, choose from the following counts to decide how many to include: {[self.word_count.options]}."
        )


class ClauseTemplate(BaseModel):
    name: str
    description: str
    instruction: str
    language: str
    components: list[Component]

    def to_llm_text(self) -> str:

        return self.instruction + "\n".join([_.to_llm_text() for _ in self.components])


# TODO: fill in the to_llm_text functions
# Each structure should be able to turn itself into an llm text object
# Add tests, and rebase this brach so that those changes were made first (clean up the mess)
# Add mask_options: Mode hint_options: Mode
# Add tags
# Ask model to return CEFR level
# document the models!
# move some of the ClauseTemplate-level instructions into the Component

# you've made a lot of progress, but this needs tidying up