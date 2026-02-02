# module.py

class LibraryBook():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def status(self):
        print(f"{self.title} by {self.author} is available:", self.available)

    def checkout(self):
        if self.available == True:
            print("Book checked out.")
            self.available = False

    def return_book(self):
        self.available = True
        print("Book returned.")
