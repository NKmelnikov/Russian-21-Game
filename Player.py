import random
from Cards import Cards


class Player:
    score: int = 0

    def __init__(self):
        self.cards = Cards()

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score

    def take_card(self):
        suit = random.choice(list(self.cards.card_desk.keys()))
        nominal = random.choice(self.cards.card_desk[suit])
        self.cards.update_card_desk(suit, nominal)
        print(suit + ' ' + nominal)
        self.count_score(nominal)

    def count_score(self, nominal):
        try:
            score = int(nominal)
        except ValueError:
            score = 10
            if nominal == 'ace':
                score = 11

        self.add_score(score)

