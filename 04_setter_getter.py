class Person:
    def __init__(self, name):
        self._name = name
        self._phone = None

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        assert isinstance(new_name, str), "Name has to be string type!"
        self._name = new_name


csaba = Person("Csaba")
csaba.set_name(42)

print(csaba.get_name())