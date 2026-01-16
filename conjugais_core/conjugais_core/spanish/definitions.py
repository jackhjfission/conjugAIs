from functools import partial

from conjugais_core.core import Option

SPANISH = "SPANISH"

SpanishOption = partial(Option, language=SPANISH)
