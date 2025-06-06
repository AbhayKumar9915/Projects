a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

index = 1

for i in range(len(b)):
    a.insert(index, b[i])
    index += 2

print(a)
