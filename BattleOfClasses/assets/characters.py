import random
from faker import Faker
faker = Faker()


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

    def report(self):
        print("-"*50)
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Inventory: {self.inventory}")
        print(f"Golds: {self.golds}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Defense: {self.defense}")
        print(f"XP: {self.xp}")
        print("-" * 50)

    def attack(self, target):
        attack_strength = random.randint(0, self.strength)

        if attack_strength == 0:
            print(f"{self.name} misses {target}")
        else:
            target.health -= attack_strength
            print(f"{self.name} hits {target} with {attack_strength} strength.")

    def __repr__(self):
        return self.name


class NPC(BaseCharacter):
    def __init__(self):
        super().__init__()

        self.name = faker.name()
        self.race = random.choice([i for i in self.RACES])
        self.init_states()


class Player(BaseCharacter):
    def __init__(self, name=None, race=None):
        super().__init__()

        if not name:
            name = input("What is your name?")
        self.name = name

        if not race:
            race = input(f"What is your race? {self.RACES.keys()}")
        self.race = race

        self.init_states()

    def buy(self):
        pass


class Enemy(NPC):
    pass


if __name__ == '__main__':
    player = Player(name="Robert", race="human")
    player.report()

    enemy = Enemy()
    enemy.report()