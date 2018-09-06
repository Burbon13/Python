from service.book_service import BookService
from service.client_service import ClientService
from ui.console import Console
from tests.py_unit_tests import *
import string
import random

chars = string.ascii_letters
books_repo = BookRepository("BookRepo.txt")
clients_repo = ClientRepository("ClientRepo.txt")
rentals_repo = Rentals("RentalRepo.txt")
rental_validator = RentalValidator()
book_validator = BookValidator()
client_validator = ClientValidator()
book_service = BookService(books_repo, book_validator)
client_service = ClientService(clients_repo, client_validator)
rental_service = RentalService(rentals_repo, rental_validator, books_repo, clients_repo)

'''
for i in range(200):
    id = random.randint(1,100)
    name = ''.join((random.choice(string.ascii_uppercase)) for x in range(4))
    cnp = random.randint(1000000000000,2999999999999)
    try:
        client_service.addClient(id,name,cnp)
    except Exception:
        pass


for i in range(2000):
    id = random.randint(1, 1000)
    title = ''.join((random.choice(chars)) for x in range(3))
    author = ''.join((random.choice(chars)) for x in range(3))
    description = ''.join((random.choice(chars)) for x in range(3))
    try:
        book_service.addBook(id,title,author,description)
        book_service.getBook(id).setRentedTimes(random.randint(1,300))
    except Exception:
        pass

for i in range(10000):
    idBook = random.randint(1, 100)
    idRenderer = random.randint(1, 10000)
    try:
        rental_service.rentBook(idBook,idRenderer)
        #rental_validator.validateRental(BookRental(idRenderer,idBook),clients_repo,books_repo)
        #rentals_repo.store(BookRental(idRenderer,idBook))
        #books_repo.getBookById(idBook).setIsRented(True)
    except Exception:
        pass
'''

console = Console(book_service, client_service, rental_service)
console.run()