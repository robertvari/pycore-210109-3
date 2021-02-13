class Person:
    name = "Robert"
    phone = "0620 555 6699"
    address = "Budapest"

    def print_person(self):
        print(self.name, self.phone, self.address)

    def say_hello(self, name):
        print(f"Hello {name}! I'm {self.name}")
        self.name = name
        self.print_person()

    def local_variables(self):
        name = "Kriszta"
        print(name)

    @staticmethod
    def hello_world():
        print("hello world", Person.name)


person = Person()
person.say_hello("Kriszta")
person.local_variables()