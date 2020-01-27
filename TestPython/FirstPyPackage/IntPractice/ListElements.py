#Sum of all elements in a list
def add(items):
    sum1 =0
    for x in items:
        sum1 = sum1 + x 
    return sum1

list1 = [5,6,8,-1]
print(add(list1))

#Multiplication of all elements in a list
def multiply(items):
    multi = 1
    for i in items:
        multi = multi*i
    return multi

print(multiply(list1))