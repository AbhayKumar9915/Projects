"""
super() - builtin returns a proxy object (temporary object of the superclass)
that allows us to access methods of the base class
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Person\'s Name is {} and age is {}'.format(self.name, self.age))


class Employee(Person):
    def __init__(self, name, age, id):
        # calling constructor of super class
        super().__init__(name, age)
        self.id = id

    def displayMethod(self):
        print('Employee\'s Name is {}, Age is {} and Id is {}'.format(self.name, self.age, self.id))


per = Person('Ravi', 28)
per.display()
emp = Employee('Abhay', 25, 1)
emp.displayMethod()
