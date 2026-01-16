from typing import TypedDict

from conjugais_core.core.clause_template_model import Option


class NounPronounBehaviour(TypedDict):
    none: Option
    nouns: Option
    pronouns: Option
    nouns_and_pronouns: Option


noun_and_pronoun_behaviour = NounPronounBehaviour(
    none=Option(
        name="None",
        instruction="Do not explicitly use subject nouns or pronouns.",
        description="In Spanish, subject pronouns can be inferred from the verb conjugation, making them optional in most contexts.",
    ),
    nouns=Option(
        name="nouns",
        instruction="Explicitly use one or more nouns. Do not use pronouns.",
        description="In Spanish specific nouns can be used as subjects, direct objects or indirect objects.",
    ),
    pronouns=Option(
        name="pronouns",
        instruction="Explicitly use one or more pronouns. Do not use nouns.",
        description="In Spanish specific pronouns can be used as subjects, direct objects or indirect objects.",
    ),
    nouns_and_pronouns=Option(
        name="nouns_and_pronouns",
        instruction="Use both nouns and pronouns together.",
        description="In Spanish, nouns and pronouns can both be used together for emphasis or clarity.",
    ),
)
