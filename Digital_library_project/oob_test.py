from Digital_library import *

The_Nun = Book("The Nun", "Manas Ranjan Sahoo", 123456 , True)
The_Moron = Book("The Moron", "Sandeep Pradhan", 560204 , False)



print(The_Nun)
print(The_Moron)

print(The_Nun.is_available())
print(The_Moron.is_available())

The_Moron.mark_unavailable()
The_Nun.mark_unavailable()
The_Nun.mark_available()
The_Nun.mark_available()

Library = Library()
Library.add_book(The_Nun)
