class Person:
    def __init__(self):
        self._name = None
        self._phone = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        print("Set name", new_name)
        self._name = new_name


csaba = Person()
csaba.name = "Kriszta"
print(csaba.name)
