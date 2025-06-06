# Bubble sort
def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(0, (len(lst)-1)-i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst


lt = [25, 12, 89, 45, 35]
print(bubbleSort(lt))


# Selection sort
def selectionSort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst


ls = [5, 3, 8, 4, 2, 6]
print(selectionSort(ls))
