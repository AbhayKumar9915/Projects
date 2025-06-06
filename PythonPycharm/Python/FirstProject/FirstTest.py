#Reverse string with for loop
def reverse(str0):
    str1=''
    for ch in str0:
        str1 = ch +str1
    return print(str1)
print("1. --- String Reverse ---")
reverse('Abhay')

#Reverse string with recursion
def reversed1(str2):
    if len(str2) == 0:
        return str2
    else:
        return reversed1(str2[1:]) + str2[0]
print(reversed1('Akshita'))

#Factorial with recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
print("2. --- Factorial ---")
print(fact(5))

#Bubble Sort
def bubblesort(list1):
    for i in range(len(list1)):
        for j in range(0, (len(list1)-1)-i):
            if list1[j]>list1[j+1]:
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return list1
print("3. --- Bubble sort ---")
print(bubblesort([5,6,4,1,8,7]))

#Selection Sort
def selection(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                tmp=lst[i]
                lst[i]=lst[j]
                lst[j]=tmp
    return lst
print("4. --- Selection sort ---")
print(selection([2,4,3,8,5,7,6,9]))

#Decorator
def decor(func):
    def inner(a,b):
        if b == 0:
            print("Can't divide by 0")
        else:
            return func(a,b)
    return inner

@decor
def div(a,b):
    return print(a/b)
print("5. --- Decorator ---")
div(5,2)
div(4,0)
div(5,8)

#Fibonacci series using generators
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
print("6. --- Fibonacci series using Generator ---")
fib=fibonacci()
for i in range(10):
    print(next(fib), end=' ')

