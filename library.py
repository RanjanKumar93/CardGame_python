class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                self.books.remove(b)
                break

    def search_books(self, search_string):
        found_books = []
        search_string = search_string.lower()
        for book in self.books:
            if (
                search_string in book.title.lower()
                or search_string in book.author.lower()
            ):
                found_books.append(book)
        return found_books


### Example Usage

# Create a few Book instances
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Create a Library instance
library = Library("City Library")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books by title
found_books = library.search_books("1984")
for book in found_books:
    print(f"Found Book: {book.title} by {book.author}")

# Remove a book
library.remove_book(book2)

# Try searching for the removed book
found_books = library.search_books("1984")
if not found_books:
    print("No books found.")
