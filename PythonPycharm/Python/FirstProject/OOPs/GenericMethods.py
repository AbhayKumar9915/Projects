class Book:
    def __init__(self, name):
        self.name = name


class Newspaper:
    def __init__(self,name):
        self.name = name

b1 = Book('The Nun')
b2 = Book('Maths')
n1 = Newspaper('Hindustan Times')

print('***type***')
print(type(b1))
print(type(n1))
print(type(b1) == type(n1))
print(type(b2) == type(b1))
print('***isinstance***')
print(isinstance(n1, object))
print(isinstance(n1, Book))
print(isinstance(n1, Newspaper))
print('***id***')
print(id(b1))
print(id(b2))
