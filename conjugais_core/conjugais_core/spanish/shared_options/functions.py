from typing import TypedDict

from conjugais_core.core import WordFunction


class BasicFunction(TypedDict):
    subject: WordFunction
    direct_object: WordFunction
    indirect_object: WordFunction
    main_verb: WordFunction
    wildcard: WordFunction


basic_function = BasicFunction(
    subject=WordFunction(
        name="subject",
        description="The subject indicates who or what is performing the verb's action.",
    ),
    direct_object=WordFunction(
        name="direct_object",
        description="The object indicates who or what is receiving the verb's action.",
    ),
    indirect_object=WordFunction(
        name="indirect_object",
        description="The indirect object indicates to whom or for whom an action is done.",
    ),
    main_verb=WordFunction(
        name="main_verb",
        description="The main verb indicates the primary action of the sentence.",
    ),
    wildcard=WordFunction(
        name="wildcard",
        description=(
            "Wildcards can be used to supplement the other word types which are explicitly specified to make "
            "sentences sound more natural and provide further translation practice."
        ),
    ),
)
