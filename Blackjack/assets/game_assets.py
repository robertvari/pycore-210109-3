class Player:
    pass


class Deck:
    pass


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

    def __str__(self):
        return f"{self.name} {self.value}"


if __name__ == '__main__':
    card = Card("Spade", 8)
    print(card)