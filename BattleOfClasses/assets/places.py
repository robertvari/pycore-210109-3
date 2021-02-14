from assets.characters import Enemy, NPC


class BasePlace:
    def __init__(self, game):
        self._game = game
        self.place_name = None
        self.player = None

    def enter(self, player):
        print(f"Welcome in the {self.place_name} {player}")
        self.player = player


class Arena(BasePlace):
    def __init__(self, game):
        super().__init__(game)
        self.place_name = "Arena"
        self._enemy = Enemy()

    def enter(self, player):
        super().enter(player)
        print(f"{self._enemy} attacks you as soon as you enter...")

        self.fight()

    def fight(self):
        winner = None

        while True:
            self._enemy.attack(self.player)

            if self.player.health <= 0:
                winner = self._enemy
                break

            self.player.attack(self._enemy)
            if self._enemy.health <= 0:
                winner = self.player
                break

        print(f"The winner is {winner}")
        self._game.menu()


class Tavern(BasePlace):
    def __init__(self, game):
        super().__init__(game)
        self.place_name = "Tavern"
        self._bartender = NPC()