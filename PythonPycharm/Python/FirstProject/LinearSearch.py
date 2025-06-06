def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1
lst1 = [5, 1, 8, 6, 9]
key1 = int(input('Enter the key to search: '))
index = linear_search(lst1, key1)
if index == -1:
    print('{} was not found.'.format(key1))
else:
    print('{} was found at index {}.'.format(key1, index))


def linear_search01(lt, key):
    for i in range(len(lt)):
        if lt[i] == key:
            return print(i)
    return print('key not in list')
linear_search01([5, 1, 4, 7, 8, 3], 7)
