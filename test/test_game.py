import settings
from game import Game

WORD = 'TEST'

def test_guess_limit_setter():
    g = Game(word=WORD, guess_limit=10)
    assert g.guess_limit == 10


def test_incorrect_guess_decrements_guess_limit():
    g = Game(word=WORD, guess_limit=10)
    assert g.guess_limit == 10
    g._guess('L')
    assert g.guess_limit == 9


def test_correct_guess_ignores_guess_limit():
    g = Game(word=WORD, guess_limit=10)
    assert g.guess_limit == 10
    g._guess('T')
    assert g.guess_limit == 10


def test_correct_guess_returns_game_word():
    g = Game(word=WORD, guess_limit=10)
    assert g._guess('T') == 'T__T'


def test_incorrect_guess_returns_failure_message():
    g = Game(word=WORD, guess_limit=10)
    assert g._guess('L') == settings.FAILED_GUESS_MESSAGE
