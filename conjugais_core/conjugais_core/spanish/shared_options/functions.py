from typing import TypedDict

from conjugais_core.core import Option


class BasicFunction(TypedDict):
    subject: Option
    direct_object: Option
    indirect_object: Option
    main_verb: Option
    wildcard: Option


basic_function = BasicFunction(
    subject=Option(
        name="subject",
        instruction="Include a subject in the sentence.",
        description="The subject indicates who or what is performing the verb's action.",
    ),
    direct_object=Option(
        name="direct_object",
        instruction="Include a direct object in the sentence.",
        description="The object indicates who or what is receiving the verb's action.",
    ),
    indirect_object=Option(
        name="indirect_object",
        instruction="Include an indirect object in the sentence.",
        description="The indirect object indicates to whom or for whom an action is done.",
    ),
    main_verb=Option(
        name="main_verb",
        instruction="Include a main verb in the sentence.",
        description="The main verb indicates the primary action of the sentence.",
    ),
    wildcard=Option(
        name="wildcard",
        instruction="Include wildcard words in the sentence.",
        description=(
            "Wildcards can be used to supplement the other word types which are explicitly specified to make "
            "sentences sound more natural and provide further translation practice."
        ),
    ),
)
