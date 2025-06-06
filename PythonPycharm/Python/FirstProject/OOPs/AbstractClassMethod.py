from abc import ABC, abstractmethod

# ABC - Abstract base class(Data Abstraction can be achieved with ABC module in python)
# If there is abstract class so its compulsory to have it one or more abstract method
# Can't create object for abstract class,required subclasses to provide implementation for abstract methods


class Computer(ABC):
    @abstractmethod
    def type(self):
        print('HP Desktop')

    def processor(self):
        print('Intel i5')


class Laptop(Computer):
    def type(self):
        print('Lenovo Laptop')


try:
    obj = Computer()
    obj.processor()
except Exception as e:
    print(e)

obj1 = Laptop()
obj1.type()
obj1.processor()