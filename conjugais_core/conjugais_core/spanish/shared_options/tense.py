from conjugais_core.core.clause_template_model import Option

from ..definitions import SpanishOption

# ----------------------------------------------------------------------------
# Tense
# ----------------------------------------------------------------------------


class ImpersonalForms:

    @staticmethod
    def infinitivo() -> Option:
        return SpanishOption(
            name="infinitivo",
            instruction="Use the Spanish infinitive",
            description="The base form of the verb.",
        )

    @staticmethod
    def participio() -> Option:
        return SpanishOption(
            name="participio",
            instruction="Use the Spanish participio form of the verb",
            description="Typically acts as an adverb or part of a compound verb tense (like the present continuous).",
        )

    @staticmethod
    def gerundio() -> Option:
        return SpanishOption(
            name="gerundio",
            instruction="Use the Spanish gerundio form of the verb",
            description="Primarily functions as an adjective or part of perfect tenses.",
        )


class SimpleIndicativo:

    @staticmethod
    def presente_indicativo() -> Option:
        return SpanishOption(
            name="presente_indicativo",
            instruction="Use the Spanish simple present tense in the indicative mood",
            description="Describes current actions, habits, universal truths, and near-future plans.",
        )

    @staticmethod
    def futuro() -> Option:
        return SpanishOption(
            name="futuro_indicativo",
            instruction="Use the Spanish simple future tense in the indicative mood",
            description="Describes what will or shall happen, predictions, or assumptions.",
        )

    @staticmethod
    def imperfecto() -> Option:
        return SpanishOption(
            name="imperfecto_indicativo",
            instruction="Use the Spanish imperfecto in the indicative mood",
            description="Describes ongoing, habitual, or descriptive past actions without a defined beginning or end.",
        )

    @staticmethod
    def preterito() -> Option:
        return SpanishOption(
            name="preterito_indicativo",
            instruction="Use the Spanish preterito in the indicative mood",
            description="Describes completed actions in the past with a definite beginning and end.",
        )

    @staticmethod
    def conditional() -> Option:
        return SpanishOption(
            name="conditional_indicativo",
            instruction="Use the Spanish conditional in the indicative mood",
            description="Expresses what someone would, could, or should do, used for polite requests, hypothetical situations (if clauses), expressing wishes, and speculation.",
        )
