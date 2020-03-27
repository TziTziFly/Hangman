import settings
from word import Word


class Game:
    def __init__(self, word, guess_limit):
        self.guesses_remaining = guess_limit
        self.word = Word(word=word)
        self.settings = settings
        self.game_won = False
        self.game_in_progress = True

    def __setattr__(self, key, value):
        # If the number of guesses_remaining is 0, end the game:
        if key == 'guesses_remaining' and value == 0:
            self.game_in_progress = False
        super().__setattr__(key, value)


    def _guess(self, letter):
        """
        Interfaces with Word class to handle guesses
        """
        result = self.word.guess(letter)
        # Game won:
        if self.word.last_guess_correct == True:
            if self.word.word_guessed:
                self.game_in_progress = False
                self.game_won = True
            return result
        # Game lost:
        else:
            self.guesses_remaining -= 1
            return self.settings.FAILED_GUESS_MESSAGE.format(self.guesses_remaining)
