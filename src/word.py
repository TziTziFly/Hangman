class Word:
    def __init__(self, word):
        self.word = word
        self._game_word = ['_'] * len(self.word)

        self.last_guess_correct = False
        self.word_guessed = False

    def word_guessed_check(self):
        if not '_' in self._game_word:
            self.word_guessed = True

    def guess(self, letter):
        self.last_guess_correct = False

        # TODO: See if a recursive solution is cleaner:
        pos = 0
        while True:
            i = self.word.find(letter, pos)
            if i == -1:
                self.word_guessed_check()
                return ''.join(self._game_word)
            else:
                self.last_guess_correct = True
            self._game_word[i] = letter
            pos = i + 1

