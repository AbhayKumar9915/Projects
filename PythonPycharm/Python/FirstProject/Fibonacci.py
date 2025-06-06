import time

print('*****Generator*****')
def fibonacci():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2
fib = fibonacci()
for i in range(10):
    print(next(fib), end=' ')
    time.sleep(1)


print('\n*****Recursion*****')
def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)
count = int(input("Enter the terms: "))
if count <= 0:
    print("Enter a number greater than 0")
else:
    for i in range(count):
        time.sleep(1)
        print(fib(i), end=" ")


print('\n*****Fibonacci till given Number*****')
def fibonacci_terms(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
fibonacci_terms(10)

