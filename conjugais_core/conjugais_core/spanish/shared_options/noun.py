from conjugais_core.core.clause_template_model import Option

# ----------------------------------------------------------------------------
# Pronoun usage
# ----------------------------------------------------------------------------


class NounPronounBehaviour:
    @staticmethod
    def none() -> Option:
        return Option(
            name="None",
            instruction="Do not explicitly use subject nouns or pronouns.",
            description="In Spanish, subject pronouns can be inferred from the verb conjugation, making them optional in most contexts.",
        )

    @staticmethod
    def nouns() -> Option:
        return Option(
            name="nouns",
            instruction="Explicitly use one or more nouns. Do not use pronouns.",
            description="In Spanish specific nouns can be used as subjects, direct objects or indirect objects.",
        )

    @staticmethod
    def pronouns() -> Option:
        return Option(
            name="pronouns",
            instruction="Explicitly use one or more pronouns. Do not use nouns.",
            description="In Spanish specific pronouns can be used as subjects, direct objects or indirect objects.",
        )

    @staticmethod
    def nouns_and_pronouns() -> Option:
        return Option(
            name="nouns_and_pronouns",
            instruction="Use both nouns and pronouns together.",
            description="In Spanish, nouns and pronouns can both be used together for emphasis or clarity.",
        )
