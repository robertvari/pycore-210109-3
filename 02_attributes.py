class Person:
    name = "Robert"

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        self._id = 123456

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.address}"


csaba = Person("CSaba", "0620 555 66 88", "Budapest")
laci = Person("Laci", "0620 666 7788", "Debrecen")

print(Person.name)
Person.name = "Kriszta"
print(Person.name)