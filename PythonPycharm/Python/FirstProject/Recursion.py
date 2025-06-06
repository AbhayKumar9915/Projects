# Recursion is when function calls itself, its loop through data to reach result.

# factorial
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


# String reverse with recursion
def rev(string):
    if len(string) <= 0:
        return string
    else:
        return rev(string[1:]) + string[0]
print(rev('Abhay'))


#Sum of digit of given number
def sum_num(n):
    if n==0:
        return 0
    else:
        return sum_num(n//10) + n%10
print("Sum of digit of given number: ",sum_num(1234))


# Fibonacci with recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

count = int(input('Enter number of term: '))

if count <= 0:
    print("Enter +ve number")
else:
    for i in range(count):
        print(fibonacci(i), end=' ')
