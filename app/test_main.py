import pytest

from main import greeting


@pytest.mark.parametrize(('name', 'expected'),
                         [('Никита', 'Greetings, Никита'),
                          ('Ольга', 'Greetings, Ольга')])
def test_greeting(name: str, expected: str):
    """Result depends on input."""
    assert greeting(name) == expected


def test_capitalize():
    """All words should be capitalized."""
    name = 'яндекс практикум'
    assert greeting(name) == 'Greetings, Яндекс Практикум'
