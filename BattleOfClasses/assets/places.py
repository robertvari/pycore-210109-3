from assets.characters import Enemy, NPC


class BasePlace:
    def __init__(self):
        self.place_name = None
        self.player = None

    def enter(self, player):
        print(f"Welcome in the {self.place_name} {player}")
        self.player = player


class Arena(BasePlace):
    def __init__(self):
        super().__init__()
        self.place_name = "Arena"
        self._enemy = Enemy()

    def enter(self, player):
        super().enter(player)
        print(f"{self._enemy} attacks you as soon as you enter...")

        while True:
            self._enemy.attack(self.player)

            if self.player.health <= 0:
                break

            self.player.attack(self._enemy)
            if self._enemy.health <= 0:
                break


class Tavern(BasePlace):
    def __init__(self):
        super().__init__()
        self.place_name = "Tavern"
        self._bartender = NPC()