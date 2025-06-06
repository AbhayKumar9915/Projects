# largest number in list
def maximum(list1):
    max1 = list1[0]
    for i in list1:
        if i > max1:
            max1 = i
    return max1


b = [5, 2, 9, 6, 10, 8]
print("Largest value is:", maximum(b))


# smallest number in list
def minimum(list1):
    min1 = list1[0]
    for i in list1:
        if i < min1:
            min1 = i
    return min1


print("Smallest value is:", minimum(b))
