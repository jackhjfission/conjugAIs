from typing import TypedDict

from conjugais_core.core import ModeOption


class Person(TypedDict):
    first_person_singular: ModeOption
    second_person_singular: ModeOption
    second_person_singular_polite: ModeOption
    third_person_singular: ModeOption
    first_person_plural: ModeOption
    second_person_plural: ModeOption
    second_person_plural_polite: ModeOption
    third_person_plural: ModeOption


person = Person(
    first_person_singular=ModeOption(
        name="first_person_singular",
        instruction="Use the Spanish first person singular conjugation.",
        description="Corresponds to 'yo' (I). Used when the speaker refers to themselves performing the action.",
    ),
    second_person_singular=ModeOption(
        name="second_person_singular",
        instruction="Use the Spanish second person singular conjugation.",
        description="Corresponds to 'tú' (you, informal). Used when addressing one person in a familiar or casual context.",
    ),
    second_person_singular_polite=ModeOption(
        name="second_person_singular_polite",
        instruction="Use the Spanish second person singular conjugation for polite address.",
        description="Corresponds to 'usted' (you, formal). Used when addressing one person in a formal, respectful, or professional context.",
    ),
    third_person_singular=ModeOption(
        name="third_person_singular",
        instruction="Use the Spanish third person singular conjugation.",
        description="Corresponds to 'él/ella' (he/she/it). Used when referring to one person or thing other than the speaker or addressee.",
    ),
    first_person_plural=ModeOption(
        name="first_person_plural",
        instruction="Use the Spanish first person plural conjugation.",
        description="Corresponds to 'nosotros/nosotras' (we). Used when the speaker includes themselves in a group performing the action.",
    ),
    second_person_plural=ModeOption(
        name="second_person_plural",
        instruction="Use the Spanish second person plural conjugation.",
        description="Corresponds to 'vosotros/vosotras' (you all, informal). Used when addressing multiple people in a familiar or casual context, primarily in Spain.",
    ),
    second_person_plural_polite=ModeOption(
        name="second_person_plural_polite",
        instruction="Use the Spanish second person plural conjugation for polite address.",
        description="Corresponds to 'ustedes' (you all, formal). Used when addressing multiple people in a formal context, or any group in Latin America.",
    ),
    third_person_plural=ModeOption(
        name="third_person_plural",
        instruction="Use the Spanish third person plural conjugation.",
        description="Corresponds to 'ellos/ellas' (they). Used when referring to multiple people or things other than the speaker or addressee.",
    ),
)
