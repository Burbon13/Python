from domain.book import *
from domain.client import *
from repository.book_repo import *
from repository.client_repo import *
from validators.book_validator import *
from validators.client_validator import *
from domain.book_rental import BookRental
from repository.rentals_repo import *
from validators.rental_validator import *


def test_Book():
    ct1 = Book(1, "Ion", "Liviu Rebreanu", "O carte de bac")
    ct2 = Book(1, "a", "a", "a")
    ct3 = Book(2, "b", "b", "b")

    assert ct1.getTitle() == "Ion"
    assert ct1.getAuthor() == "Liviu Rebreanu"
    assert ct1.getIdentity() == 1
    assert ct1.getDescription() == "O carte de bac"
    assert ct1 == ct2
    assert ct2 != ct3


def test_Client():
    cl1 = Client(1, "Razvan Roatis", 1980713080010)
    cl2 = Client(1,"b",2)
    cl3 = Client(2,"c",4)

    assert cl1.getIdentity() == 1
    assert cl1.getName() == "Razvan Roatis"
    assert cl1.getSsn() == 1980713080010
    assert cl1 == cl2
    assert cl2 != cl3


def test_BookRepository():
    book_repo = BookRepository("EmptyBookRepo.txt")

    assert book_repo.size() == 0

    try:
        book_repo.store(Book(1, "a", "a", "a"))
        assert True
    except BookRepositoryException:
        assert False

    try:
        book_repo.store(Book(1, "a", "a", "a"))
        assert False
    except BookRepositoryException as bre:
        assert str(bre) == "Cartea de adaugat exista in repo deja!"

    try:
        book_repo.store(Book(2, "a", "a", "a"))
        assert True
    except BookRepositoryException:
        assert False

    assert book_repo.size() == 2
    assert book_repo.getAllBooks() == {1: Book(1, "", "", ""), 2: Book(2, "", "", "")}
    assert book_repo.getAllBooks() != {1: Book(1, "", "", ""), 2: Book(3, "", "", "")}

    book_repo.store(Book(5, "Ion", "Rebreanu", "O carte"))

    assert book_repo.getBookById(5) == Book(5, "Ion", "Rebreanu", "O carte")


def test_ClientRepository():
    client_repo = ClientRepository()

    assert client_repo.size() == 0

    try:
        client_repo.store(Client(1, "a", 145435))
        assert True
    except ClientRepositoryException:
        assert False

    try:
        client_repo.store(Client(1, "a", 5346))
        assert False
    except ClientRepositoryException as bre:
        assert str(bre) == "Clientul de adaugat exista in repo deja!"

    try:
        client_repo.store(Client(2, "a", "a"))
        assert True
    except BookRepositoryException:
        assert False

    assert client_repo.size() == 2
    assert client_repo.getAllClients() == {1: Client(1, "", ""), 2: Client(2, "", "")}
    assert client_repo.getAllClients() != {1: Client(1, "", ""), 2: Client(3, "", "")}

    client_repo.store(Client(4, "", ""))

    assert client_repo.getClientById(4) == Client(4, "", "")


def test_BookValidator():
    book = Book(1, "Ion", "Liviu", "O carte")

    try:
        BookValidator.validateBook(book)
        assert True
    except BookValidatorException:
        assert False

    book = Book(-1,"","","Nicio carte")

    try:
        BookValidator.validateBook(book)
        assert False
    except BookValidatorException as bve:
        assert str(bve) == "Identitatea cartii trebuie sa fie un numar natural strict pozitiv!\n" \
                      "Titlul cartii trebuie sa fie diferit de nul!\nAutorul cartii trebuie sa fie diferit de nul!\n"


def test_ClientValidator():
    client = Client(1,"Vaslie",1980713080010)

    try:
        ClientValidator.validateClient(client)
        assert True
    except ClientValidatorException:
        assert False

    client = Client(-5, "", 198070010)

    try:
        ClientValidator.validateClient(client)
        assert False
    except ClientValidatorException as cve:
        assert str(cve) == "Identitatea clientului trebuie sa fie un numar natural stict pozitiv!\n" \
                           "Numele clientului trebuie sa fie diferit de nul!\n" \
                           "CNP invalid!\n"

def test_BookRental():
    brental = BookRental(6,4)

    assert brental.getBookId() == 4
    assert brental.getClientId() == 6
    brental.setBookId(5)
    brental.setClientId(7)
    assert brental.getBookId() == 5
    assert brental.getClientId() == 7


def test_Rentals():
    rrepo = Rentals()

    try:
        rrepo.store(BookRental(1,1))
        assert True
    except RentalsException:
        assert False

    try:
        rrepo.store(BookRental(2,4))
        assert True
    except RentalsException:
        assert False

    try:
        rrepo.store(BookRental(2,4))
        assert False
    except RentalsException as re:
        assert str(re) == "Inchirierea exista deja in repo!"


def test_RentalValidator():
    client_repo = ClientRepository()
    books_repo = BookRepository("EmptyBookRepo.txt")

    client_repo.store(Client(1,"",""))
    client_repo.store(Client(4, "", ""))
    client_repo.store(Client(10, "", ""))

    books_repo.store(Book(2,"","",""))
    books_repo.store(Book(7, "", "", ""))
    books_repo.store(Book(12, "", "", ""))

    bk = Book(77,"","","")
    bk.setIsRented(True)

    assert bk.getRentedTimes() == 1

    books_repo.store(bk)

    try:
        RentalValidator.validateRental(BookRental(2, 7), client_repo, books_repo)
        assert False
    except RentalValidatorException as rve:
        assert str(rve) == "Clientul nu exista in repo!\n"

    try:
        RentalValidator.validateRental(BookRental(4, 4), client_repo, books_repo)
        assert False
    except RentalValidatorException as rve:
        assert str(rve) == "Cartea nu exista in repo!\n"

    try:
        RentalValidator.validateRental(BookRental(4, 77), client_repo, books_repo)
        assert False
    except RentalValidatorException as rve:
        assert str(rve) == "Cartea este deja inchiriata!\n"

    try:
        RentalValidator.validateRental(BookRental(1, 2), client_repo, books_repo)
        assert True
    except RentalValidatorException as rve:
        assert False

    try:
        RentalValidator.validateRental(BookRental(44, 43), client_repo, books_repo)
        assert False
    except RentalValidatorException as rve:
        assert str(rve) == "Clientul nu exista in repo!\nCartea nu exista in repo!\n"


def teste_TopRentedBooks():
    pass

def runTests():
    test_Client()
    test_Book()
    test_BookRepository()
    test_ClientRepository()
    test_BookValidator()
    test_ClientValidator()
    test_BookRental()
    test_Rentals()
    test_RentalValidator()
    teste_TopRentedBooks()