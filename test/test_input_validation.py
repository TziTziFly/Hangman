import pytest

from game import Game, UserFacingException


WORD = 'TEST'
G = Game(WORD, 10)

def test_lowercase_is_converted_to_uppercase():
        assert G._validate_input('x') == 'X'


def test_multiple_character_guess_raises_error():
    with pytest.raises(UserFacingException,
            match=G.settings.ERROR_INPUT_LENGTH_TOO_LONG):
        G._validate_input('XX')


def test_zero_character_guess_raises_error():
    with pytest.raises(UserFacingException,
            match=G.settings.ERROR_INPUT_LENGTH_TOO_SHORT):
        G._validate_input('')


def test_number_input_raises_error():
    with pytest.raises(UserFacingException,
            match=G.settings.ERROR_INPUT_NON_ALPHA):
        G._validate_input('1')


def test_punctuation_input_raises_error():
    with pytest.raises(UserFacingException,
            match=G.settings.ERROR_INPUT_NON_ALPHA):
        G._validate_input(';')


def test_previously_used_guess_raises_error():
    # this is a different Game object because guesses are no longer idempotent
    game = Game(WORD, 10)
    letter = 'P'
    game.previous_guesses.add(letter)
    with pytest.raises(UserFacingException,
            match=G.settings.ERROR_PREVIOUSLY_GUESSED.format(letter)):
        game._validate_input(letter)


def test_previously_used_mid_game_guess_raises_error():
    game = Game(WORD, 10)
    letter = 'L'
    game.previous_guesses.add(letter)
    exception_message = game.settings.ERROR_PREVIOUSLY_GUESSED.format(letter)
    with pytest.raises(UserFacingException, match=exception_message):
        game._validate_input('L')
