from typing import TypedDict

from conjugais_core.core.clause_template_model import ModeOption


class ImpersonalForms(TypedDict):
    infinitivo: ModeOption
    participio: ModeOption
    gerundio: ModeOption


class SimpleIndicativo(TypedDict):
    presente: ModeOption
    futuro: ModeOption
    imperfecto: ModeOption
    preterito: ModeOption
    conditional: ModeOption


impersonal_forms = ImpersonalForms(
    infinitivo=ModeOption(
        name="infinitivo",
        instruction="Use the Spanish infinitive.",
        description="The base form of the verb.",
    ),
    participio=ModeOption(
        name="participio",
        instruction="Use the Spanish participio form of the verb.",
        description="Typically acts as an adverb or part of a compound verb tense (like the present continuous).",
    ),
    gerundio=ModeOption(
        name="gerundio",
        instruction="Use the Spanish gerundio form of the verb.",
        description="Primarily functions as an adjective or part of perfect tenses.",
    ),
)


simple_indicativo = SimpleIndicativo(
    presente=ModeOption(
        name="presente_indicativo",
        instruction="Use the Spanish simple present tense in the indicative mood.",
        description="Describes current actions, habits, universal truths, and near-future plans.",
    ),
    futuro=ModeOption(
        name="futuro_indicativo",
        instruction="Use the Spanish simple future tense in the indicative mood.",
        description="Describes what will or shall happen, predictions, or assumptions.",
    ),
    imperfecto=ModeOption(
        name="imperfecto_indicativo",
        instruction="Use the Spanish imperfecto in the indicative mood.",
        description="Describes ongoing, habitual, or descriptive past actions without a defined beginning or end.",
    ),
    preterito=ModeOption(
        name="preterito_indicativo",
        instruction="Use the Spanish preterito in the indicative mood.",
        description="Describes completed actions in the past with a definite beginning and end.",
    ),
    conditional=ModeOption(
        name="conditional_indicativo",
        instruction="Use the Spanish conditional in the indicative mood.",
        description="Expresses what someone would, could, or should do, used for polite requests, hypothetical situations (if clauses), expressing wishes, and speculation.",
    ),
)
