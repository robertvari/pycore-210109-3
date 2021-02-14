from assets.game_assets import Deck, Player


class Blackjack:
    def __init__(self):
        self._intro()
        self._players = [
            Player().create(),
            Player().create(),
            Player().create(),
        ]

        self.deck = Deck()
        self.current_bet = 0

        self.player = None

        self._create_player()

        self.game()

    def _create_player(self):
        name = "Robert Vari"
        self.player = Player().create(name)
        print(f"Welcome in the game. You have {self.player.wallet}")
        print(f"You are playing with {self._players}")

    def game(self):

        for player in self._players:
            print(f"{player} is in game.")

            self.current_bet += player.give_bet(10)

            while player.in_game:
                player.get_card(self.deck)

            player.report()

    @staticmethod
    def _intro():
        print("*" * 50, "Blackjack", "*" * 50)


if __name__ == '__main__':
    Blackjack()
