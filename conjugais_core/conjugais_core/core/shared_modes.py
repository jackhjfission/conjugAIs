from .clause_template_model import Mode, ModeOption


def word_count(min_: int, max_: int) -> Mode:

    return Mode(
        name="count",
        description="The number of words to use.",
        options=[
            ModeOption(
                name=f"{_}",
                instruction=(
                    f"Use {_} of this word type in the sentence. The count of words should not be strictly enforced and must "
                    "defer to other grammatical selections. For instance, if the first person singular is used then the number "
                    "of nouns used as the subject of the sentence must be one and any other value specified by this option can be "
                    "ignored."
                ),
                description="",
            )
            for _ in range(min_, max_ + 1)
        ],
        is_choice=True,
    )
