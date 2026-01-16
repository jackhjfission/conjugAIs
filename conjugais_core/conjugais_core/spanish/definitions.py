from functools import partial
from textwrap import dedent

from conjugais_core.core import ClauseTemplate

SPANISH = "SPANISH"

SPANISH_CLAUSE_INSTRUCTIONS = dedent(
    """**Spanish language general instructions**

    Your aim is to create grammatically correct and satisfying sentences in Spanish for a learner.
    Follow the instructions provided by the clause template to generate a sentence.

    If any `mode` contains multiple options you can select the option at random.

    If any `word_options` contains multiple options you can select according to the `count`. However the `count` of subjects must agree
    with the `person`. If a specific `person` is requested with an inconsistent `count` of subjects then the `count` of subjects must be disregarded.

    If the `word_options` contains no words then choose vocabulary yourself based on the previous logic.

    Note the `optional` attribute represents whether a particular component is necessary in a sentence.

    **Subjects are always optional in Spanish** because they can be inferred from verb conjugation:
    - Example: "Trabajo en Madrid" (I work in Madrid) - no explicit subject, implied from verb ending
    - Example: "Habían estado comiendo" (They had been eating) - no explicit subject

    The `mode` with `name` "subject_noun_pronoun" specifies this behaviour. However, there are examples in Spanish
    of sentences with no subject (implicit or explicit). eg:
    - Example: "Llueve" (It's raining) - no subject exists
    - Example: "Se dice que..." (It is said that...) - Impersonal "se" construction, no subject exists

    Use your judgement based on the available verbs to include a subject or not.

    **Direct objects are optional** when using intransitive verbs:
    - Example: "Duermo bien" (I sleep well) - no direct object needed
    - Example: "Corremos cada día" (We run every day) - no direct object needed

    **Indirect objects are optional** in most sentences:
    - Example: "Como una manzana" (I eat an apple) - has direct object, no indirect object
    - Example: "Leí el libro" (I read the book) - has direct object, no indirect object

    Use your judgement on whether to include subjects, direct objects and indirect objects based on natural Spanish usage. If you
    choose to include them, aim to include the number specified in `count` for that `function`. However,
    as mentioned, defer to the `person` for the subject.

    Vary gender for the purpose of practice.

    Articles and adjectives _must_ agree with their nouns in gender and number.

    **In general, maintaining the grammatical rules of Spanish is the highest priority, above the specification of a sentence provided.**
    """
)

SpanishClauseTemplate = partial(ClauseTemplate, instruction=SPANISH_CLAUSE_INSTRUCTIONS)
