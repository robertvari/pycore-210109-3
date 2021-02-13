class Vehicles:
    def __init__(self):
        self.type = None
        self.speed = None
        self.color = None
        self.doors = 4

    def print_data(self):
        print(self.type, self.speed, self.color, self.doors)


class Cars(Vehicles):
    def __init__(self, type, speed, color):
        super().__init__()
        self.type = type
        self.speed = speed
        self.color = color


class Bike(Vehicles):
    def __init__(self, type, speed, color):
        super().__init__()
        self.type = type
        self.speed = speed
        self.color = color

        self.doors = None

    def print_data(self):
        print("Hello I'M a bike!")


my_car = Cars("Audi", 100, "Red")
your_car = Cars("Mercedes", 150, "Blue")

my_bike = Bike("Csepel", 10, "White")

my_car.print_data()
your_car.print_data()

my_bike.print_data()