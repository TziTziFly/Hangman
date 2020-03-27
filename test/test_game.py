from game import Game

WORD = 'TEST'

def test_correct_guess():
    g = Game(WORD)
    assert g.guess('T') == 'T__T'


def test_incorrect_guess():
    g = Game(WORD)
    assert g.guess('Z') == '____'
