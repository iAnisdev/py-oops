from library.staff import Staff, Librarian, Assistant
from library.book import Book
from library.member import Member


def isStaff(staff):
    return isinstance(staff, Staff)


def isLibrarian(staff):
    return isinstance(staff, Librarian)


def isAssistant(staff):
    return isinstance(staff, Assistant)


def isBook(book):
    return isinstance(book, Book)


def isMember(member):
    return isinstance(member, Member)
