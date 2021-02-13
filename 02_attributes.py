class Person:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address


csaba = Person("CSaba", "0620 555 66 88", "Budapest")
laci = Person("Laci", "0620 666 7788", "Debrecen")

print(csaba.name, csaba.phone, csaba.address)
print(laci.name, laci.phone, laci.address)