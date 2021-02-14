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

    def give_bet(self, value):
        self.wallet -= value

        return value

    def get_card(self, deck):
        hand_value = self._count_hand()

        if hand_value > 16:
            self.in_game = False
            print(f"{self.name} passes...")
        else:
            new_card = deck.give_card()

            print(f"{self.name} got {new_card}")

            if "Ace" in new_card.name and hand_value > 10:
                new_card.value = 1

            self.hand.append(new_card)

    def report(self):
        print(f"{self.name} hand value: {self._count_hand()}")

    def _count_hand(self):
        return sum([card.value for card in self.hand])

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

    def give_card(self):
        current_card = self.cards[-1]
        self.cards.remove(current_card)
        return current_card

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

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return f"{self.name} {self.value}"


if __name__ == '__main__':
    deck = Deck()

    player1 = Player().create()
    player2 = Player().create()
    player3 = Player().create()
    player4 = Player().create()

    players = [player1, player2, player3, player4]

    for p in players:
        print(f"{p} is playing...")
        while p.in_game:
            p.get_card(deck)

    player1.report()
    player2.report()
    player3.report()
    player4.report()