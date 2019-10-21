from Player import Player


class Game:
    playing = True
    instruction = """
    Welcome to Russian `21` Game
    press `t` to take a card
    press `o` to open cards
    press `x` to exit
    """

    def __init__(self):
        self.player1 = Player()
        self.dealer = Player()

    def dealer_plays(self):
        while self.dealer.get_score() < 19:
            self.dealer.take_card()

    def result(self):
        self.dealer_plays()

        pl_score = self.player1.get_score()
        d_score = self.dealer.get_score()
        print('Your score is %d' % pl_score)
        print('Dealer`s score is: %d' % d_score)
        if pl_score == 21 and d_score == 21:
            print('Draw, both win')
        elif pl_score > 21 and d_score > 21:
            print('Draw, both lost')
        elif 21 >= pl_score > 17 and 21 >= d_score > 17:
            if pl_score > d_score:
                print('You win!')
            else:
                print('Dealer win)')
        elif 21 >= pl_score > 17 and d_score > 21:
            print('You win!')
        elif 21 >= d_score > 17 and pl_score > 21:
            print('Dealer win)')
        else:
            print('Unknown result')

    def play(self):
        print(self.instruction)
        while self.playing:
            user_input = input('type a command: ')
            if user_input == 't':
                self.player1.take_card()
            elif user_input == 'o':
                self.result()
                exit()
            elif user_input == 'x':
                print('Good bye :)')
                exit()
            else:
                print('There is no such command')


game = Game()
game.play()
