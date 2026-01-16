from approvaltests import verify_as_json

from conjugais_core.spanish import basic_clause_templates


def test_simple_tenses() -> None:
    verify_as_json(basic_clause_templates.simple_tenses.model_dump(mode="json"))
