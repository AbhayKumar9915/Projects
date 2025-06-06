#A set is an unordered, mutable collection that does not allow duplicate values.

my_set = {7, 5, 2, 8, 6, 2}
for i in my_set:
    print(i)
print(my_set)

my_set.add(3)
print(my_set)
my_set.remove(8)
print(my_set)
print(my_set.pop())