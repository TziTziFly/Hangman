class Word:
    def __init__(self, word):
        self._word = word
        self._game_word = ['_'] * len(self._word)

        self.last_guess_correct = False

    def guess(self, letter):
        self.last_guess_correct = False

        # TODO: See if a recursive solution is cleaner:
        pos = 0
        while True:
            i = self._word.find(letter, pos)
            if i == -1:
                return ''.join(self._game_word)
            else:
                self.last_guess_correct = True
            self._game_word[i] = letter
            pos = i + 1

