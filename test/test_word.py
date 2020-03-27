from word import Word

WORD = 'TEST'


def test_correct_guess():
    w = Word(WORD)
    assert w.guess('T') == 'T__T'


def test_incorrect_guess():
    w = Word(WORD)
    assert w.guess('Z') == '____'
