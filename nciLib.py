from library.index import Library
from library.staff import Librarian

nci = Library("NCI", "Dublin")

# add admin to the library
admin = nci.addAdmin()
john = nci.addStaff(admin.id, Librarian("john", "librarian"))
print(nci.staff)
nci.removeStaff(admin.id, john.id)
print(nci.staff)




