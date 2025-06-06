"""Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
Method overloading is not possible in python (way to create multiple methods with the
same name but different arguments)
Method Overriding is possible by using inheritance - Same method name with different characteristics.
"""


class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)