class MyClass:
    name = "Csaba"


my_class = MyClass()
my_class2 = MyClass()
my_class3 = MyClass()

my_class2.name = "Robert"
my_class2.age = 42

print(my_class.name)
print(my_class2.name)
print(my_class2.age)
print(my_class3.name)

print(MyClass.name)