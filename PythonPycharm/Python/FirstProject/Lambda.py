"""
Lambda Function
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Example...
list = [1,2,3,4,5]
filter - [2,4] - filtered some value from sequence on checking true false conditions(Even numbers filtered)
map - [2,4,6,8,10] - applied operation on each values in sequence (multiplied by 2)
reduce - 15 - applied operation inside sequence on values (sum of all values)
"""

#Filter
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 2, 6]

'''
Always check for True and false
Python filter() function is used to get filtered elements. This function takes two arguments, 
first is a function and the second is iterable. The filter function returns a sequence from those 
elements of iterable for which function returns True.
'''

# Filter function using defined function isEven
s1 = set(filter(isEven, list1))  # Set returning value after removing duplication in random order
# Filter function with using Lambda expression,only one line code
l1 = list(filter(lambda a: a % 2 == 0, list1))  # List and Tuple returning all values fulfilling conditions
t1 = tuple(filter(lambda i: i % 2 != 0, list1))  # Odd value condition
print("*** Lambda with Filter ***")
print(s1)
print(l1)
print(t1)


#MAP
def double(x):
    return 2*x
list2 = [4, 5, 7, 3, 9, 4, 5, 2]

'''
Never check for True and false, Apply on every iterable and gives output
Python map() function is used to return a list of results after applying a given 
function to each item of an iterable
'''
# Map function using defined function double
s1 = set(map(double, list2))  # Set returning value after removing duplication in random order
# Map function with using Lambda expression,only one line code
l1 = list(map(lambda a: a*2, list2))  # List and Tuple returning all values fulfilling conditions
t1 = tuple(map(lambda i: i*3, list2))  # No checks for duplication
print("*** Lambda with MAP ***")
print(s1)
print(l1)
print(t1)


# Map can be applied more than one iterable sequence,should have same number of iterable
m1 = [1, 2, 3, 4, 5]
m2 = [10, 20, 30, 40, 50]
m3 = list(map(lambda x, y: x*y, m1, m2))
print(m3)


#Reduce
from functools import reduce
"""
Reduce(fun,seq) function is used to apply a particular function passed 
in its argument to all of the list elements mentioned in the sequence passed along.
This function is defined in “functools” module.
"""
list3 = [1, 2, 3, 4, 5]
s1 = reduce(lambda a, b: a+b, list3)
print("*** Lambda with Reduce ***")
print(s1)

s2 = reduce(lambda a, b: a+b, range(0, 101))  # sum of 0 to 100
print(s2)
