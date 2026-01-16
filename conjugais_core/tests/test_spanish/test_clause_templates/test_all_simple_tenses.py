from approvaltests import verify_as_json

from conjugais_core.spanish.clause_templates import all_simple_tenses


def test_all_simple_tenses() -> None:
    verify_as_json(all_simple_tenses.all_simple_tenses.model_dump(mode="json"))
