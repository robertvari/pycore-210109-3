from assets.characters import Player


class BattleOfClasses:
    def __init__(self):
        self.player = Player()

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
            pass
        elif player_input == "2":
            pass


if __name__ == '__main__':
    BattleOfClasses()