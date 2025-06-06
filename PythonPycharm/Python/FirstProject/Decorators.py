"""
Input Fn -> Decorator Fn -> Fn With Extended Functionality
Decorators are used to extend the functionality of existing function without changing its
own property,Decorators allow us to wrap another function in order to extend the behavior of
wrapped function, without permanently modifying it.
"""


def decor(func):  # Decorator Fn
    def inner(a, b):
        if b == 0:
            print("Can't divide by Zero")
        else:
            return func(a, b)
    return inner


@decor  # @ made link between both decorator and existing fn
def div(a, b):  # Existing Fn
    return print(a/b)


div(5, 2)
div(6, 0)
div(10, 3)

"""
One object can be made for decorator and existing fn so existing function and
decorator fn can be used separately 
decorator_Fn = decor(div)
decorator_Fn(9,0)
div(5,0)
"""
