
with open(r'C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\ReadData\\Test.txt', 'r') as rf:
    data = rf.read()
    data = data.lower()
    d = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        v = 0
        for j in data:
            if j == i:
                v = v + 1
                d[i] = v
    print(d)





