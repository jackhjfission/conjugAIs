from conjugais_core.core import Component
from conjugais_core.core.shared_modes import word_count

from . import modes
from .shared_options import functions

subject = Component(
    word_options=[],
    function=functions.BasicFunction.subject(),
    modes=[word_count(min_=1, max_=2), modes.NounPronounBehaviour.subject()],
    optional=False,
)

direct_object = Component(
    word_options=[],
    function=functions.BasicFunction.direct_object(),
    modes=[word_count(min_=1, max_=2), modes.NounPronounBehaviour.object()],
    optional=True,
)

indirect_object = Component(
    word_options=[],
    function=functions.BasicFunction.indirect_object(),
    modes=[word_count(min_=1, max_=2), modes.NounPronounBehaviour.object()],
    optional=True,
)

main_verb = Component(
    word_options=[],
    function=functions.BasicFunction.main_verb(),
    modes=[
        modes.Person.all_person(),
        modes.Tense.all_simple_indicativo(),
        word_count(min_=1, max_=1),
    ],
    optional=False,
)

wildcard = Component(
    word_options=[],
    function=functions.BasicFunction.wildcard(),
    modes=[
        word_count(min_=1, max_=2),
    ],
    optional=True,
)
