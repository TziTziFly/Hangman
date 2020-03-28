import settings
from word import Word


class UserFacingException(Exception):
    pass


class Game:
    def __init__(self, word, guess_limit):
        self.guesses_remaining = guess_limit
        self.word = Word(word=word)
        self.settings = settings
        self.game_won = False
        self.game_in_progress = True
        self.previous_guesses = set()

    def __setattr__(self, key, value):
        # If the number of guesses_remaining is 0, end the game:
        if key == 'guesses_remaining' and value == 0:
            self.game_in_progress = False
        super().__setattr__(key, value)


    # TODO: Refactor this:
    def _validate_input(self, letter):
        if len(letter) > 1:
            raise UserFacingException(self.settings.ERROR_INPUT_LENGTH_TOO_LONG)
        elif len(letter) < 1:
            raise UserFacingException(self.settings.ERROR_INPUT_LENGTH_TOO_SHORT)
        else:
            if not letter.isalpha():
                raise UserFacingException(self.settings.ERROR_INPUT_NON_ALPHA)

            if letter.islower():
                letter = letter.upper()

            if letter in self.previous_guesses:
                if len(self.previous_guesses) > 1:
                    # Append previous guesses to message if there're more than one:
                    raise UserFacingException (
                            self.settings.ERROR_PREVIOUSLY_GUESSED.format(letter) +
                            ' ' +
                            self.settings.PREVIOUSLY_GUESSED_CLAUSE.format(
                                sorted(self.previous_guesses - set(letter))))
                # Otherise, just raise error without settings.PREVIOUSLY_GUESSED_CLAUSE:
                raise UserFacingException(self.settings.ERROR_PREVIOUSLY_GUESSED.format(letter))
            return letter


    def _guess(self, letter):
        """
        Interfaces with Word class to handle guesses
        """
        try:
            letter = self._validate_input(letter)
        except UserFacingException as e:
            return str(e)

        result = self.word.guess(letter)
        # Game won:
        if self.word.last_guess_correct == True:
            if self.word.word_guessed:
                self.game_in_progress = False
                self.game_won = True
            return result
        # Game lost:
        else:
            self.previous_guesses.add(letter)
            self.guesses_remaining -= 1
            return self.settings.FAILED_GUESS_MESSAGE.format(self.guesses_remaining)
