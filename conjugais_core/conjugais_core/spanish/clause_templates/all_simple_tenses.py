from conjugais_core.core import Component
from conjugais_core.core.shared_modes import word_count

from .. import modes
from ..definitions import SPANISH, SpanishClauseTemplate
from ..shared_options import functions

all_simple_tenses = SpanishClauseTemplate(
    name="simple_tenses",
    description="Practice of all Spanish simple tenses.",
    language=SPANISH,
    components=[
        Component(
            word_options=[],
            word_function=functions.basic_function["main_verb"],
            modes=[
                modes.Person.all_person(),
                modes.Tense.all_simple_indicativo(),
            ],
            optional=False,
            word_count=word_count(min_=1, max_=1),
        ),
        Component(
            word_options=[],
            word_function=functions.basic_function["subject"],
            modes=[modes.NounPronounBehaviour.subject()],
            optional=True,
            word_count=word_count(min_=1, max_=2),
        ),
        Component(
            word_options=[],
            word_function=functions.basic_function["direct_object"],
            modes=[modes.NounPronounBehaviour.object()],
            optional=True,
            word_count=word_count(min_=1, max_=2),
        ),
        Component(
            word_options=[],
            word_function=functions.basic_function["indirect_object"],
            modes=[modes.NounPronounBehaviour.object()],
            optional=True,
            word_count=word_count(min_=1, max_=2),
        ),
        Component(
            word_options=[],
            word_function=functions.basic_function["wildcard"],
            modes=[],
            optional=True,
            word_count=word_count(min_=1, max_=2),
        ),
    ],
)
