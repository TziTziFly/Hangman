class Game:
    def __init__(self, word):
        self.WORD = word
        self.GAME_WORD = ['_'] * len(self.WORD)

    def guess(self, letter):
        # TODO: See if a recursive solution is cleaner:
        pos = 0
        while True:
            i = self.WORD.find(letter, pos)
            if i == -1:
                return ''.join(self.GAME_WORD)
            self.GAME_WORD[i] = letter
            pos = i + 1

