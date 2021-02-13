from assets.game_assets import Deck, Player


class Blackjack:
    def __init__(self):
        self._intro()
        self._players = []
        self._current_level = 0

        self.deck = Deck()
        self.current_bet = 0

        self.player = Player()

    @staticmethod
    def _intro():
        print("*" * 50, "Blackjack", "*" * 50)


if __name__ == '__main__':
    Blackjack()
