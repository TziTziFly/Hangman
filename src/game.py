import settings
from word import Word


class Game:
    def __init__(self, word, guess_limit):
        self.guess_limit = guess_limit
        self.word = Word(word=word)

    def _guess(self, letter):
        """
        Interfaces with Word class to handle guesses
        """
        result = self.word.guess(letter)
        if self.word.last_guess_correct == True:
            return result
        else:
            self.guess_limit -= 1
            return settings.FAILED_GUESS_MESSAGE
