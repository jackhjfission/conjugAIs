from conjugais_core.core import ClauseTemplate

from . import basic_components
from .definitions import SPANISH

simple_tenses = ClauseTemplate(
    name="simple_tenses",
    description="Practice of all Spanish simple tenses.",
    language=SPANISH,
    components=[
        basic_components.main_verb,
        basic_components.subject,
        basic_components.direct_object,
        basic_components.indirect_object,
        basic_components.wildcard,
    ],
)
