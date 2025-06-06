lst = [1, 3, 4, 5, 6, 7, 2, 3, 4, 5, 2, 3]
st = set(lst)

# Counting occurrence of each number in list and storing in dict
d = {}
for i in st:
    count = 0
    for j in lst:
        if i == j:
            count = count + 1
            d[i] = count
print(d)

# Printing duplicate values from list
for i in st:
    count = 0
    for j in lst:
        if i == j:
            count = count + 1
    if count > 1:
        print(i, end=' ')
