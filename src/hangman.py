from game import Game

def main():
    g = Game('TEST', 3)
    print(g.settings.TITLE)
    while g.game_in_progress:
            guess = input(g.settings.INPUT_GUESS_MESSAGE)
            result = g._guess(guess)
            print(result)
    else:
        if g.game_won:
            print(g.settings.WIN_MESSAGE)
        else:
            print(g.settings.LOSE_MESSAGE)
            print(g.settings.WORD_REVEAL_MESSAGE.format(g.word.word))
        print(g.settings.GOODBYE_MESSAGE)


if __name__ == '__main__':
    main()
