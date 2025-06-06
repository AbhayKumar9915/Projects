def fact1(n):
    if n == 0:
        return 1
    else:
        return n * fact1(n-1)


print(fact1(5))

print('*****Factorial Without Recursion*****')


def fact(n):
    factorial = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            factorial = factorial * i
        return factorial


print(fact(6))
