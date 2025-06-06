"""
Using OOP in Python, we can restrict access to methods and variables,
This prevents data from direct modification which is called encapsulation,
In Python, we denote private attributes using underscore as the prefix i.e. single _ or double __
"""


class Computer:

    def __init__(self):
        self.__maxPrice = 1000

    def sell(self):
        print('Selling price is {}'.format(self.__maxPrice))

    def setmaxPrice(self, price):
        self.__maxPrice = price


com = Computer()
com.sell()

# Try changing the price directly(Can't change its private variable)
com.__maxPrice = 900
com.sell()

# Change price using setter fn
com.setmaxPrice(900)
com.sell()
