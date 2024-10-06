from library.utils import uniqueId


class Member:
    def __init__(self, name, email):
        self.id = uniqueId()
        self.email = email
        self.name = name
        self.borrowed_books = []

    def assignBook(self, book):
        self.borrowed_books.append(book.id)

    def returnBook(self, book):
        if book.id in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            raise TypeError("Book is not borrowed by the member")

    def viewBorrowedBooks(self):
        return self.borrowed_books

    def isBorrowed(self, book):
        return book.id in self.borrowed_books
