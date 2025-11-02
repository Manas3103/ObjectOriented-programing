class Book:
    def __init__(self, title, author, isbn, available):   # if i write the isbn as 123-345 then self.isbn only prints -345
        self.title = title
        self.author = author
        self.isbn = isbn #This is the International Standard Book Number
        self.available = available

    def __str__(self):
        if self.available == True:
            return f"The '{self.title}' is written by '{self.author}' with the ISBN number '{self.isbn}' is available"
        else:
            return f"The '{self.title}' is written by '{self.author}' with the ISBN number '{self.isbn}' is not available"

    def is_available(self):
        return self.available

    def mark_unavailable(self):
        if self.available:
            self.available = False
            print(f"The {self.title} is not available")
        elif not self.available:
            print(f"Error The {self.title} is Already unavailable")
        else:
            print("The book is not listed") #this is not working if the object has not been created then it shows the name error

    def mark_available(self):
        if not self.available:
            self.available = True
            print(f"The {self.title} is available")
        elif self.available == True:
            print(f"Error The {self.title} is already available")
        else:
            print("The book is not listed") #this is not working if the object has not been created then it shows the name error

            
            
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book.title)
        print(f"The {book.title} has been added to the library.\nNow anyone can access this.")


    
