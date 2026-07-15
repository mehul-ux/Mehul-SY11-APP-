# Library Management System using OOP

# Book Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"ID: {self.book_id}, Title: {self.title}, "
              f"Author: {self.author}, Status: {status}")


# Patron Class
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


# Library Class
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully!")

    # Register new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print("Patron registered successfully!")

    # Issue book
    def issue_book(self, book_id, patron_id):
        if book_id in self.books and patron_id in self.patrons:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.available:
                book.available = False
                patron.borrowed_books.append(book.title)
                print(f"Book '{book.title}' issued to {patron.name}.")
            else:
                print("Book is already issued.")
        else:
            print("Invalid Book ID or Patron ID.")

    # Return book
    def return_book(self, book_id, patron_id):
        if book_id in self.books and patron_id in self.patrons:
            book = self.books[book_id]
            patron = self.patrons[patron_id]

            if book.title in patron.borrowed_books:
                book.available = True
                patron.borrowed_books.remove(book.title)
                print(f"Book '{book.title}' returned successfully.")
            else:
                print("This patron did not borrow the book.")
        else:
            print("Invalid Book ID or Patron ID.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            book.display()


# Driver Program
library = Library()

# Adding Books
b1 = Book(101, "Python Programming", "Guido Van Rossum")
b2 = Book(102, "Data Structures", "Mark Allen")

library.add_book(b1)
library.add_book(b2)

# Registering Patrons
p1 = Patron(1, "Rahul")
p2 = Patron(2, "Sneha")

library.register_patron(p1)
library.register_patron(p2)

# Display Books
library.display_books()

# Issue Book
library.issue_book(101, 1)

# Display Patron Details
p1.display()

# Return Book
library.return_book(101, 1)

# Display Books Again
library.display_books()