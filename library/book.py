from library.utils import uniqueId


class Book:
    def __init__(self, title, genre, copies):
        self.id = uniqueId()
        self.title = title
        self.genre = genre
        self.totalCopies = copies
        self.assignedLibrary = None
        self.availableCopies = copies
        self.borrowedBy = []

    def isAvailable(self):
        return self.availableCopies > 0

    def assignBookToLibrary(self, library):
        if self.assignBookToLibrary == None:
            self.assignedLibrary = library.id
        else:
            raise TypeError("Book is already assigned to another library!")

    def assignBookToUser(self, member):
        if self.isAvailable():
            self.borrowedBy.append(member.id)
            self.availableCopies -= 1
        else:
            raise TypeError("Book is not available!")

    def unAssignBookFromUser(self, member):
        if member.id in self.borrowedBy:
            self.borrowedBy.remove(member.id)
            self.availableCopies += 1
        else:
            raise TypeError("Book is not assigned to this user!")
