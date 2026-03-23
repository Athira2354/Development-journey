"""
Create a class Book with a constructor that initializes title and author. Display the book details.

"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
book1 = Book("Randamoozham ", "MT Vasudevan Nair")
book1.display_details()
book2 = Book("Aadujeevitham", "Benyamin")
book2.display_details()