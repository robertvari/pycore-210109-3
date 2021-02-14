from assets.game_assets import Deck, Player, RealPlayer


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
        self.player = RealPlayer().create(name)
        print(f"You are playing with {self._players}")

    def game(self):
        print(f"Welcome in the game. You have {self.player.wallet} credits.")

        for player in self._players:
            print(f"{player} is in game.")

            self.current_bet += player.give_bet(10)
            player.get_start_hand(self.deck)
            player.get_card(self.deck)

        print(f"\nNow this is your turn {self.player}")
        self.current_bet += self.player.give_bet(10)
        self.player.get_start_hand(self.deck)
        self.player.get_card(self.deck)

        print("-"*50)
        self.player.report()

        for i in self._players:
            i.report()

        self.get_winner()

        is_continue = input("Do you want to continue?(y/n)")

        if is_continue == "y":
            self.deck.create()
            self.player.drop_hand()
            [i.drop_hand() for i in self._players]
            self.game()
        else:
            print("Maybe next time!")

    def get_winner(self):
        player_list = [i for i in self._players]
        player_list.append(self.player)
        player_list = [i for i in player_list if i.hand_value <= 21]

        if player_list:
            winner_list = sorted(player_list, key=lambda p: p.hand_value)
            winner = winner_list[-1]
            print(f"The winner is {winner} who wins {self.current_bet} credits")
            winner.wallet += self.current_bet
        else:
            print("Nobody wins.")

    @staticmethod
    def _intro():
        print("*" * 50, "Blackjack", "*" * 50)


if __name__ == '__main__':
    Blackjack()
