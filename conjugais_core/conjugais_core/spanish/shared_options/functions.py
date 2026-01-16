from conjugais_core.core import Option


class BasicFunction:

    @staticmethod
    def subject() -> Option:
        return Option(
            name="subject",
            instruction="Include a subject in the sentence.",
            description="The subject indicates who or what is performing the verb's action.",
        )

    @staticmethod
    def direct_object() -> Option:
        return Option(
            name="direct_object",
            instruction="Include a direct object in the sentence.",
            description="The object indicates who or what is receiving the verb's action.",
        )

    @staticmethod
    def indirect_object() -> Option:
        return Option(
            name="indirect_object",
            instruction="Include an indirect object in the sentence.",
            description="The indirect object indicates to whom or for whom an action is done.",
        )

    @staticmethod
    def main_verb() -> Option:
        return Option(
            name="main_verb",
            instruction="Include a main verb in the sentence.",
            description="The main verb indicates the primary action of the sentence.",
        )

    @staticmethod
    def wildcard() -> Option:
        return Option(
            name="wildcard",
            instruction="Include wildcard words in the sentence.",
            description=(
                "Wildcards can be used to supplement the other word types which are explicitly specified to make "
                "sentences sound more natural and provide further translation practice."
            ),
        )
