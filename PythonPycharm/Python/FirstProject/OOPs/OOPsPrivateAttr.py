class Book:

    def __init__(self, title, author, price, page):
        self.title = title
        self.author = author
        self.price = price
        self.page = page
        self.__secret = "This is secret"

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self, _discount):
        self._discount = _discount
        '''Making discount attribute as private with using single underscore by 
        which it can be used under the class only and can't be modified'''


b1 = Book('Math Mystery', 'Abhay', 25.55, 500)
b2 = Book('The Nun', 'Ravi', 75.35, 250)

print(b1.getPrice())
print(b2.getPrice())
b2.setDiscount(0.25)
print(b2.getPrice())

try:
    print(b2.__secret)
except Exception as e:
    print(e)
print(b2._Book__secret)
