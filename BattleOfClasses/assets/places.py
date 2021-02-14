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
        self.enemy = Enemy()

    def enter(self, player):
        super().enter(player)


class Tavern(BasePlace):
    def __init__(self):
        super().__init__()
        self.place_name = "Tavern"
        self.bartender = NPC()