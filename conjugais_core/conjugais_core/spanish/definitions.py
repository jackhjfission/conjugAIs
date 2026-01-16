from functools import partial

from conjugais_core.core import Option
from conjugais_core.core.shared_modes import count

SPANISH = "SPANISH"

SpanishOption = partial(Option, language=SPANISH)

spanish_count = partial(count, language=SPANISH)
