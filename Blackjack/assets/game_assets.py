import random
from faker import Faker


class Player:
    def __init__(self):
        self.name = None
        self.wallet = random.randint(100, 1000)
        self.hand = []
        self.in_game = True

        self._fake = Faker()

    def create(self, name=None):
        if name:
            self.name = name
        else:
            self.name = self._fake.name()

        return self

    def __repr__(self):
        return self.name

class Deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        self.cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card in cards:
                card_name = f"{name} {card[0]}"
                value = card[1]

                self.cards.append(Card(card_name, value))

        random.shuffle(self.cards)

    def __str__(self):
        return str(self.cards)


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return f"{self.name} {self.value}"


if __name__ == '__main__':
    deck = Deck()

    player1 = Player().create("Robert Vari")
    player2 = Player().create()
    player3 = Player().create()
    player4 = Player().create()

    print(player1)
    print(player2)
    print(player3)
    print(player4)