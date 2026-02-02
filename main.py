# main.py
import os
os.system("clear")
# Do not modify code above this line.

from module import LibraryBook

# TODO 1: Book titles are not showing correctly in Section 1.
# TODO 2: The checkout method crashes the program.
# TODO 3: Books can be checked out even if they are already checked out.
# TODO 4: The status method is not printing anything.

# Create book instances
b1 = LibraryBook("1984", "George Orwell")
b2 = LibraryBook("The Hobbit", "J.R.R. Tolkien")

print("SECTION 1\n")
print("Title:", b1.title)
print("Author:", b1.author)
b1.status

print()

print("Title:", b2.title)
print("Author:", b2.author)
b2.status

print("-----------------------------------\n")

print("SECTION 2\n")
b1.checkout()
print("After checkout, available:", b1.available)

print()

b1.checkout()
print("After second checkout, available:", b1.available)

print("-----------------------------------\n")

print("SECTION 3\n")
b2.checkout()
print("After checkout, available:", b2.available)

b2.return_book()
print("After return, available:", b2.available)
