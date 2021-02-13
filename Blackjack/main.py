class Blackjack:
    def __init__(self):
        self._intro()
        self._players = []
        self._current_level = 0

    @staticmethod
    def _intro():
        print("*" * 50, "Blackjack", "*" * 50)


if __name__ == '__main__':
    Blackjack()
