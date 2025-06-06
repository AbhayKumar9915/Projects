import time
"""
Generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
Python Generators are the functions that return the traversal object and used to create iterators.
It traverses the entire items at once, and its uses yield keyword instead return.
Improves Performance
Memory Utilization improved
Easy to use
"""


# Example 1
def fibonacci():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1+num2


fib = fibonacci()
for i in range(10):
    print(next(fib), end=' ')

# # Example 2
# lst = [2, 4, 6]
# a = (x*x for x in lst)
# print(a)
# print(next(a))  # next and  __next__ used to call next iterator
# print(a.__next__())
# print(next(a))
# print('*'*10)
#
#
# # Example 3
# def timeCounter():
#     for i in range(3):
#         yield i
#
#
# for j in timeCounter():
#     print(j)
#     time.sleep(1)
