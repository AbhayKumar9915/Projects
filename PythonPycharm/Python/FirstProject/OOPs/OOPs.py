class Employee:
    # Class is a Blueprint/Template or prototype on which objects are created
    company = 'TCS'  # Static Variable/Class level variable(Inside Class)

    '''__init__ is a special method in Python classes, it is the constructor method for a class, 
    it used to initialize object state and variables'''
    def __init__(self, name, age):
        self.name = name  # Instance Variable/Object level variable(Inside Constructor)
        self.age = age

    '''The self parameter is a reference to the current instance of the class,                 
    and is used to access variables that belongs to the class.
    It does not have to be named self, can give it any name'''

    def display(self):
        salary = 40000  # Local Variable/Method level variable(Inside Method/Temporary Variable,No self keyword req)
        print('My Name is: {} and my Age is: {} and Salary: {} and working in {}'.format(self.name, self.age, salary, self.company))


'''An Object is an instance of a Class. A class is like a blueprint while 
an instance is a copy of the class with actual values'''
e1 = Employee('Abhay', 28)  # first object of Employee class
e2 = Employee('Ravi', 27)  # second object of Employee class

e1.display()
e2.display()
print(e1.company)
print(e2.company)

"""
[Features]      [Self]              [Object]
Where used      Inside the class    Outside the class
Refer to        Current instance    Specific instance of
                of class            class
Purpose         To access attrib    To create and interact
                utes/methods        with class data
"""

class Car: #Blueprint/Template or prototype on which objects are created
    country='India' #class level variable - Static variable
    def __init__(self,model,year): #contructor of class, used to initialize objects state and behaviour
        self.model=model #Self represents current instance of class and should be first parameter of any function
        self.year=year

    def display(self):
        state='UP' #Method level variable, self not required - Local variable
        print("Model is {} and Released in {} and launched in {}, {}".format(self.model,self.year,state, self.country))


c1=Car('Nexon',2020) #Object is instance of class with its properties and methods
c2=Car('Tiago',2022) #2nd object of class car
c1.display()
c2.display()