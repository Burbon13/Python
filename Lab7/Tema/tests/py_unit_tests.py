from domain.client import Client
from domain.book import Book
from domain.book_rental import BookRental
from repository.book_repo import BookRepository, BookRepositoryException
from repository.client_repo import ClientRepository, ClientRepositoryException
from repository.rentals_repo import Rentals, RentalsException
from validators.book_validator import BookValidator, BookValidatorException
from validators.client_validator import ClientValidatorException, ClientValidator
from validators.rental_validator import RentalValidator, RentalValidatorException
from service.rental_service import RentalService
from domain.clint_with_booksDTO import ClientBooksDTO
import unittest


class TestCaseBook(unittest.TestCase):
    def setUp(self):
        self.ct1 = Book(1, "Ion", "Liviu Rebreanu", "O carte de bac")
        self.ct2 = Book(1, "a", "a", "a")
        self.ct3 = Book(2, "b", "b", "b")

    def tearDown(self):
        pass

    def testBookNotEqual(self):
        self.assertNotEqual(self.ct2, self.ct3)

    def testBookEqual(self):
        self.assertEqual(self.ct1, self.ct2)

    def testGetTitle(self):
        self.assertEqual(self.ct1.getTitle(), "Ion")

    def testGetIdentity(self):
        self.assertEqual(self.ct1.getIdentity(), 1)

    def testGetAuthor(self):
        self.assertEqual(self.ct1.getAuthor(), "Liviu Rebreanu")

    def teseGetDescription(self):
        self.assertEqual(self.ct1.getDescription(), "O carte de bac")


class TestCaseClient(unittest.TestCase):
    def setUp(self):
        self.cl1 = Client(1, "Razvan Roatis", 1980713080010)
        self.cl2 = Client(1, "b", 2)
        self.cl3 = Client(2, "c", 4)

    def tearDown(self):
        pass

    def testClientGetIdentity(self):
        self.assertEqual(self.cl1.getIdentity(), 1)

    def testClientGetName(self):
        self.assertEqual(self.cl1.getName(), "Razvan Roatis")

    def testGetClientSsn(self):
        self.assertEqual(self.cl1.getSsn(), 1980713080010)

    def testClientEqual(self):
        self.assertEqual(self.cl1, self.cl2)

    def testClientNotEqual(self):
        self.assertNotEqual(self.cl2, self.cl3)


class TestCaseBookRepository(unittest.TestCase):
    def setUp(self):
        self.file = open("EmptyBookRepoTEST.txt", "w")
        self.book_repo = BookRepository("EmptyBookRepoTEST.txt")
        self.book_repo.store(Book(1, "a", "a", "a"))

    def tearDown(self):
        self.file.close()

    def testBookRaises(self):
        with self.assertRaises(BookRepositoryException) as bre:
            self.book_repo.store(Book(1, "a", "a", "a"))

        self.assertEqual(str(bre.exception), "Cartea de adaugat exista in repo deja!")

    def testBookRepoSize(self):
        self.book_repo.store(Book(2, "a", "a", "a"))
        self.assertEqual(self.book_repo.size(), 2)

    def testBookRepoEqual(self):
        self.book_repo.store(Book(2, "a", "a", "a"))
        self.assertEqual(self.book_repo.getAllBooks(), {1: Book(1, "", "", ""), 2: Book(2, "", "", "")})

    def testBookRepoNotEqual(self):
        self.assertNotEqual(self.book_repo.getAllBooks(), {1: Book(1, "", "", ""), 2: Book(3, "", "", "")})

    def testBookRepoEqual1(self):
        self.book_repo.store(Book(5, "Ion", "Rebreanu", "O carte"))
        self.assertEqual(self.book_repo.getBookById(5), Book(5, "Ion", "Rebreanu", "O carte"))


class TestCaseClientRepository(unittest.TestCase):
    def setUp(self):
        self.file = open("EmptyClientRepoTEST.txt", "w")
        self.client_repo = ClientRepository("EmptyClientRepoTEST.txt")
        self.client_repo.store(Client(1, "a", 145435))
        self.client_repo.store(Client(2, "a", "a"))


    def tearDown(self):
        self.file.close()

    def testRepoRaises(self):
        with self.assertRaises(ClientRepositoryException) as cre:
            self.client_repo.store(Client(1, "a", 5346))

        self.assertEqual(str(cre.exception), "Clientul de adaugat exista in repo deja!")

    def testRepoSize(self):
        self.assertEqual(self.client_repo.size(), 2)

    def testRepoEquals(self):
        self.assertEqual(self.client_repo.getAllClients(), {1: Client(1, "", ""), 2: Client(2, "", "")})

    def testRepoNotEqual(self):
        self.assertNotEqual(self.client_repo.getAllClients(), {1: Client(1, "", ""), 2: Client(3, "", "")})


class TestCaseBookValidator(unittest.TestCase):
    def setUp(self):
        self.book1 = Book(1, "Ion", "Liviu", "O carte")
        self.book2 = Book(-1,"","","Nicio carte")

    def tearDown(self):
        pass

    def testValidator(self):
        BookValidator.validateBook(self.book1)

        with self.assertRaises(BookValidatorException) as bve:
            BookValidator.validateBook(self.book2)

        self.assertEqual(str(bve.exception), "Identitatea cartii trebuie sa fie un numar natural strict pozitiv!\n" +\
                    "Titlul cartii trebuie sa fie diferit de nul!\nAutorul cartii trebuie sa fie diferit de nul!\n")


class TestCaseClientValidator(unittest.TestCase):
    def setUp(self):
        self.client1 = Client(1,"Vaslie",1980713080010)
        self.client2 = Client(-5, "", 198070010)

    def tearDown(self):
        pass

    def testValidator(self):
        ClientValidator.validateClient(self.client1)

        with self.assertRaises(ClientValidatorException) as cve:
            ClientValidator.validateClient(self.client2)

        self.assertEqual(str(cve.exception), "Identitatea clientului trebuie sa fie un numar natural stict "
                                             "pozitiv!\n" + "Numele clientului trebuie sa fie diferit de "
                                             "nul!\n" + "CNP invalid!\n")


class TestCaseBookRental(unittest.TestCase):
    def setUp(self):
        self.brental = BookRental(6, 4)

    def tearDown(self):
        pass

    def testGetBookId(self):
        self.assertEqual(self.brental.getBookId(), 4)

    def testGetClientId(self):
        self.assertEqual(self.brental.getClientId(), 6)

    def testChangeClient(self):
        self.brental.setBookId(5)
        self.assertEqual(self.brental.getBookId(), 5)

    def testChangeBook(self):
        self.brental.setClientId(7)
        self.assertEqual(self.brental.getClientId(), 7)


class TestCaseRentals(unittest.TestCase):
    def setUp(self):
        self.file = open("EmptyRentalsRepoTEST.txt", "w")
        self.rrepo = Rentals("EmptyRentalsRepoTEST.txt")
        self.rrepo.store(BookRental(1, 1))
        self.rrepo.store(BookRental(2, 4))

    def tearDown(self):
        self.file.close()

    def testValidator(self):
        with self.assertRaises(RentalsException) as re:
            self.rrepo.store(BookRental(2, 4))

        self.assertEqual(str(re.exception), "Inchirierea exista deja in repo!")


class TestCaseRentalValidator(unittest.TestCase):
    def setUp(self):
        self.fileClients = open("EmptyClientRepoTEST.txt", "w")
        self.fileBooks = open("EmptyRentalsRepoTEST.txt", "w")
        self.client_repo = ClientRepository("EmptyClientRepoTEST.txt")
        self.books_repo = BookRepository("EmptyRentalsRepoTEST.txt")

        self.client_repo.store(Client(1, "", ""))
        self.client_repo.store(Client(4, "", ""))
        self.client_repo.store(Client(10, "", ""))

        self.books_repo.store(Book(2, "", "", ""))
        self.books_repo.store(Book(7, "", "", ""))
        self.books_repo.store(Book(12, "", "", ""))

        self.bk = Book(77, "", "", "")
        self.bk.setIsRented(True)
        self.books_repo.store(self.bk)

    def tearDown(self):
        self.fileClients.close()
        self.fileBooks.close()

    def testRaiseException1(self):
        with self.assertRaises(RentalValidatorException) as rve:
            RentalValidator.validateRental(BookRental(2, 7), self.client_repo, self.books_repo)

        self.assertEqual(str(rve.exception), "Clientul nu exista in repo!\n")

    def testRaiseException2(self):
        with self.assertRaises(RentalValidatorException) as rve:
            RentalValidator.validateRental(BookRental(4, 4), self.client_repo, self.books_repo)

        self.assertEqual(str(rve.exception), "Cartea nu exista in repo!\n")

    def testRaiseException3(self):
        with self.assertRaises(RentalValidatorException) as rve:
            RentalValidator.validateRental(BookRental(4, 77), self.client_repo, self.books_repo)

        self.assertEqual(str(rve.exception), "Cartea este deja inchiriata!\n")

    def testRaiseException3(self):
        with self.assertRaises(RentalValidatorException) as rve:
            RentalValidator.validateRental(BookRental(44, 43), self.client_repo, self.books_repo)

        self.assertEqual(str(rve.exception), "Clientul nu exista in repo!\nCartea nu exista in repo!\n")


class TestCaseTopRentedBooks(unittest.TestCase):
    def setUp(self):
        self.fileBooks = open("EmptyBooksRepoTEST.txt", "w")
        books_repo = BookRepository("EmptyBooksRepoTEST.txt")
        self.fileRentals = open("EmptyRentalsRepoTEST.txt", "w")
        rentals_repo = Rentals("EmptyRentalsRepoTEST.txt")
        self.fileClients = open("EmptyClientsRepoTEST.txt", "w")
        clients_repo = ClientRepository("EmptyClientsRepoTEST.txt")
        rental_validator = RentalValidator()

        books_repo.store(Book(2, "a", "a", "a"))
        books_repo.store(Book(7, "b", "b", "b"))
        books_repo.store(Book(12, "c", "c", "c"))
        books_repo.store(Book(1, "d", "d", "d"))
        books_repo.store(Book(5, "e", "e", "e"))
        books_repo.store(Book(15, "f", "f", "f"))
        books_repo.getBookById(2).setRentedTimes(4)
        books_repo.getBookById(7).setRentedTimes(0)
        books_repo.getBookById(12).setRentedTimes(2)
        books_repo.getBookById(1).setRentedTimes(10)
        books_repo.getBookById(5).setRentedTimes(3)
        books_repo.getBookById(15).setRentedTimes(1)

        self.rental_service = RentalService(rentals_repo, rental_validator, books_repo, clients_repo)

    def tearDown(self):
        self.fileBooks.close()
        self.fileClients.close()
        self.fileRentals.close()

    def testTopBooks(self):
        self.assertEqual(self.rental_service.getMostRentedBooks(), [Book(1, "d", "d", "d"), Book(2, "a", "a", "a"), Book(5, "e", "e", "e")])


class TestCaseTopClients(unittest.TestCase):
    def setUp(self):
        self.fileBooks = open("EmptyBooksRepoTEST.txt", "w")
        books_repo = BookRepository("EmptyBooksRepoTEST.txt")
        self.fileRentals = open("EmptyRentalsRepoTEST.txt", "w")
        rentals_repo = Rentals("EmptyRentalsRepoTEST.txt")
        self.fileClients = open("EmptyClientsRepoTEST.txt", "w")
        clients_repo = ClientRepository("EmptyClientsRepoTEST.txt")
        rental_validator = RentalValidator()

        clients_repo.store(Client(1,"a",1980713080010))
        clients_repo.store(Client(2,"b",1980713080010))
        clients_repo.store(Client(3,"c",1980713080010))
        clients_repo.store(Client(4,"d",1980713080010))
        clients_repo.store(Client(5,"e",1980713080010))
        clients_repo.store(Client(6,"f",1980713080010))
        clients_repo.getClientById(1).setRentedBooks(1)
        clients_repo.getClientById(1).setRentedBooks(3)
        clients_repo.getClientById(2).setRentedBooks(3)
        clients_repo.getClientById(3).setRentedBooks(2)
        clients_repo.getClientById(4).setRentedBooks(6)
        clients_repo.getClientById(5).setRentedBooks(2)
        clients_repo.getClientById(6).setRentedBooks(1)
        books_repo.store(Book(1, "a", "a", "a"))
        books_repo.store(Book(2, "b", "b", "b"))
        books_repo.store(Book(3, "c", "c", "c"))
        books_repo.store(Book(4, "d", "d", "d"))
        books_repo.store(Book(5, "e", "e", "e"))
        books_repo.store(Book(6, "f", "f", "f"))
        books_repo.store(Book(7, "f", "f", "f"))
        rentals_repo.store(BookRental(1,1))
        rentals_repo.store(BookRental(2,2))
        rentals_repo.store(BookRental(1,3))
        rentals_repo.store(BookRental(4,4))
        rentals_repo.store(BookRental(5,5))
        rentals_repo.store(BookRental(6,6))
        rentals_repo.store(BookRental(3, 7))

        self.rental_service = RentalService(rentals_repo, rental_validator, books_repo, clients_repo)

    def tearDown(self):
        self.fileBooks.close()
        self.fileClients.close()
        self.fileRentals.close()

    def testTopClients(self):
        self.assertEqual(self.rental_service.getTopClients(), [ClientBooksDTO("a")])


class TestCaseClientsWithBooks(unittest.TestCase):
    def setUp(self):
        self.fileBooks = open("EmptyBooksRepoTEST.txt", "w")
        books_repo = BookRepository("EmptyBooksRepoTEST.txt")
        self.fileRentals = open("EmptyRentalsRepoTEST.txt", "w")
        rentals_repo = Rentals("EmptyRentalsRepoTEST.txt")
        self.fileClients = open("EmptyClientsRepoTEST.txt", "w")
        clients_repo = ClientRepository("EmptyClientsRepoTEST.txt")
        rental_validator = RentalValidator()

        clients_repo.store(Client(1, "a", 1980713080010))
        clients_repo.store(Client(2, "b", 1980713080010))
        clients_repo.store(Client(3, "c", 1980713080010))
        clients_repo.store(Client(4, "d", 1980713080010))
        clients_repo.store(Client(5, "e", 1980713080010))
        clients_repo.store(Client(6, "f", 1980713080010))
        clients_repo.getClientById(1).setRentedBooks(1)
        clients_repo.getClientById(1).setRentedBooks(3)
        clients_repo.getClientById(2).setRentedBooks(3)
        clients_repo.getClientById(2).setRentedBooks(2)
        clients_repo.getClientById(4).setRentedBooks(6)
        clients_repo.getClientById(2).setRentedBooks(2)
        clients_repo.getClientById(6).setRentedBooks(1)
        books_repo.store(Book(1, "a", "a", "a"))
        books_repo.store(Book(2, "b", "b", "b"))
        books_repo.store(Book(3, "c", "c", "c"))
        books_repo.store(Book(4, "d", "d", "d"))
        books_repo.store(Book(5, "e", "e", "e"))
        books_repo.store(Book(6, "f", "f", "f"))
        books_repo.store(Book(7, "t", "f", "f"))
        rentals_repo.store(BookRental(1, 1))
        rentals_repo.store(BookRental(2, 2))
        rentals_repo.store(BookRental(1, 3))
        rentals_repo.store(BookRental(6, 4))
        rentals_repo.store(BookRental(5, 5))
        rentals_repo.store(BookRental(6, 6))
        rentals_repo.store(BookRental(2, 7))

        self.rental_service = RentalService(rentals_repo, rental_validator, books_repo, clients_repo)

    def tearDown(self):
        self.fileBooks.close()
        self.fileClients.close()
        self.fileRentals.close()

    def testClients(self):
        self.assertEqual(self.rental_service.getClientsWithRentedBooks(0), [ClientBooksDTO("a"),ClientBooksDTO("b"),
                                                                            ClientBooksDTO("e"),ClientBooksDTO("f")])


if __name__ == '__main__':
    unittest.main()