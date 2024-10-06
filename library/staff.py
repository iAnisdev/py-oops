from library.utils import uniqueId
from enum import Enum


class StaffRoles(Enum):
    LIBRARIAN = "Librarian"
    ASSISTANT = "Assistant"


class Staff:
    def __init__(self, library, name):
        self.id = uniqueId()
        self.library = library
        self.name = name


class Librarian(Staff):
    def __init__(self, library, name):
        super().__init__(library, name)
        self.role = StaffRoles.LIBRARIAN


class Assistant(Staff):
    def __init__(self, library, name):
        super().__init__(library, name)
        self.role = StaffRoles.ASSISTANT
