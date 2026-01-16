from .clause_template_model import Mode, Option


def word_count(min_: int, max_: int) -> Mode:

    return Mode(
        name="count",
        description="The number of words to use.",
        options=[
            Option(
                name=f"{_}",
                instruction=f"Use {_} of this word type in the sentence.",
                description="",
            )
            for _ in range(min_, max_ + 1)
        ],
        is_choice=True,
    )
