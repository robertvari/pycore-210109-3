import random


class BaseCharacter:
    RACES = {
        "human": {"strength": 30, "defense": 30},
        "elf": {"strength": 40, "defense": 60},
        "ork": {"strength": 80, "defense": 65},
        "dwarf": {"strength": 50, "defense": 80}
    }

    def __init__(self):
        self.name = None
        self.race = None

        self.inventory = []
        self.golds = 0
        self.health = 100

        self.strength = 0
        self.defense = 0

        self.xp = 0

    def init_states(self):
        self.golds = random.randint(0, 100)

        assert self.race, "race must be set before init_states()"

        self.defense = self.RACES[self.race]["defense"]
        self.strength = self.RACES[self.race]["strength"]


class Player(BaseCharacter):
    def __init__(self):
        super().__init__()

        self.name = input("What is your name?")
        self.race = input(f"What is your race? {self.RACES}")


class Enemy(BaseCharacter):
    pass


class NPC(BaseCharacter):
    pass


if __name__ == '__main__':
    enemy = Enemy()