"""
*args - Non Keyword arguments, *args used in function definitions to pass an unknown number of
variable to a function, with * any value can be used but args used as standard value.
"""


def Adder(*n):  # It used when we don't know about number of variable to pass in fn
    total = 0
    for x in n:
        total = total + x
    print(total)


Adder(2)
Adder(5, 5)
Adder(5, 5, 6)
Adder(5, 5, 9, 7)
Adder(5, 5, 5, 8, 7)
print('*'*10)

"""
**kwargs  - Keyword arguments,**kwargs in function definitions is used to pass a keyword, 
variable-length argument list, like args at the place of kwargs any value can be used with **
kwargs used as dictionary that maps each keyword to the value that we pass alongside it.
"""


def display(**kwargs):
    for k, v in kwargs.items():
        print(k, ':', v)
    print()


display(n1=10, n2=20)
display(name1='Abhay', name2='Adarsh', name3='Ravi')
display(n1=5, n2=15, n3=25, n4=35)
