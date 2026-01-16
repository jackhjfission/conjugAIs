from conjugais_core.core import ClauseTemplate, Component
from conjugais_core.core.shared_modes import word_count

from .. import modes
from ..definitions import SPANISH
from ..shared_options import functions

all_simple_tenses = ClauseTemplate(
    name="simple_tenses",
    description="Practice of all Spanish simple tenses.",
    language=SPANISH,
    components=[
        Component(
            word_options=[],
            function=functions.basic_function["main_verb"],
            modes=[
                modes.Person.all_person(),
                modes.Tense.all_simple_indicativo(),
                word_count(min_=1, max_=1),
            ],
            optional=False,
        ),
        Component(
            word_options=[],
            function=functions.basic_function["subject"],
            modes=[word_count(min_=1, max_=2), modes.NounPronounBehaviour.subject()],
            optional=False,
        ),
        Component(
            word_options=[],
            function=functions.basic_function["direct_object"],
            modes=[word_count(min_=1, max_=2), modes.NounPronounBehaviour.object()],
            optional=True,
        ),
        Component(
            word_options=[],
            function=functions.basic_function["indirect_object"],
            modes=[word_count(min_=1, max_=2), modes.NounPronounBehaviour.object()],
            optional=True,
        ),
        Component(
            word_options=[],
            function=functions.basic_function["wildcard"],
            modes=[
                word_count(min_=1, max_=2),
            ],
            optional=True,
        ),
    ],
)
