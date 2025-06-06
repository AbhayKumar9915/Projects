class Book:

    BOOK_TYPE = ('Hardcover', 'Paperback', 'Ebook')

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPE

    def settitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPE:
            raise ValueError("{} is not a valid book type".format(booktype))
        else:
            self.booktype = booktype


print("Book Types: ", Book.getbooktypes())

b1 = Book("The Nun", 'Hardcover')
print(b1.booktype)

b2 = Book('Maths', 'Educational')
print(b2.booktype)

