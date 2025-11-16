from domain.greetings import build_greeting

def test_build_greeting_without_name():
    assert build_greeting(None) == "hello world"

def test_build_greeting_with_name():
    assert build_greeting("damian") == "hello damian"

def test_build_greeting_lower_case():
    assert build_greeting("Damian") == "hello damian"