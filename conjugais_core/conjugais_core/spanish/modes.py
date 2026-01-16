from conjugais_core.core import Mode

from .shared_options import noun, person, tense


class Tense:

    @staticmethod
    def all_simple_indicativo() -> Mode:
        return Mode(
            name="all_simple_indicativo",
            description="Collection of all Spanish simple indicativo tenses.",
            options=[
                tense.simple_indicativo["presente"],
                tense.simple_indicativo["preterito"],
                tense.simple_indicativo["imperfecto"],
                tense.simple_indicativo["futuro"],
                tense.simple_indicativo["conditional"],
            ],
            is_choice=True,
        )


class Person:

    @staticmethod
    def all_person() -> Mode:
        return Mode(
            name="all_person",
            description="Collection of all Spanish subject person.",
            options=[
                person.person["first_person_singular"],
                person.person["second_person_singular"],
                person.person["second_person_singular_polite"],
                person.person["third_person_singular"],
                person.person["first_person_plural"],
                person.person["second_person_plural"],
                person.person["second_person_plural_polite"],
                person.person["third_person_plural"],
            ],
            is_choice=True,
        )


class NounPronounBehaviour:

    @staticmethod
    def subject() -> Mode:
        return Mode(
            name="subject_noun_pronoun",
            description="Choice of noun or pronoun for subject.",
            options=[
                noun.noun_and_pronoun_behaviour["none"],
                noun.noun_and_pronoun_behaviour["nouns"],
                noun.noun_and_pronoun_behaviour["pronouns"],
                noun.noun_and_pronoun_behaviour["nouns_and_pronouns"],
            ],
            is_choice=True,
        )

    @staticmethod
    def object() -> Mode:
        return Mode(
            name="object_noun_pronoun",
            description="Choice of noun or pronoun for object.",
            options=[
                noun.noun_and_pronoun_behaviour["nouns"],
                noun.noun_and_pronoun_behaviour["pronouns"],
                noun.noun_and_pronoun_behaviour["nouns_and_pronouns"],
            ],
            is_choice=True,
        )
