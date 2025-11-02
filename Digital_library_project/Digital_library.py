class Book:
    def __init__(self, title, author, isbn, available):
        self.bookname = title
        self.author = author
        self.isbn = isbn #This is the International Standard Book Number
        self.available = available

    def __str__(self):
        if self.available == True:
            return f"The '{self.bookname}' is written by '{self.author}' with the ISBN number '{self.isbn}' is available"
        else:
            return f"The '{self.bookname}' is written by '{self.author}' with the ISBN number '{self.isbn}' is not available"

    
