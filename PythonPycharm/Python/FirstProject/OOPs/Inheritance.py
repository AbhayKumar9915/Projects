"""
Inheritance is a way of creating a new class for using details of an existing class without modifying it,
The newly formed class is a derived class (or child class)
"""


def swim():
    print("Swim faster")


def run():
    print("Run faster")


# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")


# child/derived class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")


swim()
run()
peggy = Penguin()
peggy.whoisThis()
