from assets.characters import Player
from assets.places import Arena, Tavern


class BattleOfClasses:
    def __init__(self):
        self.player = Player(name="Robert", race="human")
        self.arena = Arena(self)
        self.tavern = Tavern(self)

        self.intro()

    def intro(self):
        print(f"Welcome in this game {self.player}")
        self.menu()

    def menu(self):
        print("What do you want to do?")
        print("1. Enter the Arena")
        print("2. Go to the Tavern")
        print("3. Exit")

        player_input = input()
        if player_input == "3":
            exit()

        elif player_input == "1":
            self.arena.enter(self.player)

        elif player_input == "2":
            self.tavern.enter(self.player)


if __name__ == '__main__':
    BattleOfClasses()