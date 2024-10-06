from library.utils import uniqueId
from library.helpers import isStaff, isLibrarian, isAssistant, isBook, isMember
from library.staff import Librarian


class Library:
    def __init__(self, name, location):
        self.id = uniqueId()
        self.name = name
        self.location = location
        self.books = []
        self.staff = []
        self.members = []

    def addAdmin(self):
        if len(self.staff) == 0:
            try:
                admin = Librarian(self.name, "Admin")
                self.staff.append(admin.id)
                return admin
            except Exception as e:
                print(e.message)
        else:
            raise TypeError("Only new library can have admin")

    def isActiveStaff(self, staffId):
        return staffId in self.staff

    def addStaff(self, adminId, staff):
        if self.isActiveStaff(adminId):
            if isLibrarian(staff) or isAssistant(staff):
                self.staff.append(staff.id)
                return staff
            else:
                raise TypeError("Only instances of Staff can be added")
        else:
            raise TypeError("Only active staff can add staff")

    def removeStaff(self, adminId, staffId):
        if self.isActiveStaff(adminId):
            if self.isActiveStaff(staffId):
                self.staff.remove(staffId)
            else:
                raise TypeError("Staff is not active")
        else:
            raise TypeError("Only active staff can remove staff")

    def addBook(self, adminId, book):
        if self.isActiveStaff(adminId):
            if isBook(book):
                self.books.append(book.id)
            else:
                raise TypeError("Only instances of Book can be added")
        else:
            raise TypeError("Only active staff can add book")

    def removeBook(self, adminId, bookId):
        if self.isActiveStaff(adminId):
            if bookId in self.books:
                self.books.remove(bookId)
            else:
                raise TypeError("Book is not available")
        else:
            raise TypeError("Only active staff can remove book")

    def addMember(self, adminId, member):
        if self.isActiveStaff(adminId):
            if isMember(member):
                self.members.append(member.id)
            else:
                raise TypeError("Only instances of Member can be added")
        else:
            raise TypeError("Only active staff can add member")

    def removeMember(self, adminId, memberId):
        if self.isActiveStaff(adminId):
            if memberId in self.members:
                self.members.remove(memberId)
            else:
                raise TypeError("Member is not available")
        else:
            raise TypeError("Only active staff can remove member")


    def viewBooks(self):
        return self.books
    
    def viewMembers(self):

        return self.members
    
    def viewStaff(self):

        return self.staff