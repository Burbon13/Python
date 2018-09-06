from domain.book_rental import BookRental
from domain.clint_with_booksDTO import ClientBooksDTO

class RentalService:
    def __init__(self, rentals_repo, rental_validator, books_repo, clients_repo):
        self.__rentals_repo = rentals_repo
        self.__rental_validator = rental_validator
        self.__clients_repo = clients_repo
        self.__books_repo = books_repo

    def getClient(self, identity):
        '''
            Returneaza clientul cu un anumit id
            Parametri:
            identity = identitatea clientului de cautat
            Return: clientul cu id-ul identity
        '''
        return self.__clients_repo.getClientById(identity)

    def getBook(self, identity):
        '''
            Returneaza cartea cu un anumit id
            Parametri:
            identity = identitatea cartii de cautat
            Return: cartea cu id-ul identity
        '''
        return self.__books_repo.getBookById(identity)

    def rentBook(self, clientId, bookId):
        '''
            Adauga o inchiriere de carte in repo
            Parametri:
            clientId - identitatea clientului care inchiriaz, valoare naturala
            bookId - identitatea cartii inchiriata, valoare naturala
        '''
        book_rental = BookRental(clientId,bookId)
        self.__rental_validator.validateRental(book_rental, self.__clients_repo, self.__books_repo)
        self.__rentals_repo.store(book_rental)
        self.getBook(bookId).setIsRented(True)
        self.getClient(clientId).setRentedBooks(self.getClient(clientId).getRentedBooks() + 1)
        self.__books_repo.save()
        self.__clients_repo.save()

    def returnBook(self, clientId, bookId):
        '''
            Returneaza o carte de catre un client
            Parametri:
            clientId - identitatea clientului care inchiriaz, valoare naturala
            bookId - identitatea cartii inchiriata, valoare naturala
        '''
        book_rental = BookRental(clientId, bookId)
        self.__rentals_repo.delete(book_rental)
        self.getBook(bookId).setIsRented(False)
        self.getClient(clientId).setRentedBooks(self.getClient(clientId).getRentedBooks() - 1)
        self.__books_repo.save()
        self.__clients_repo.save()

    def getAllRentals(self):
        return self.__rentals_repo.getAll()

    def getMostRentedBooks(self):
        '''
            Returneaza primele 3 cele mai inchiriate carti, daca sunt mai putine, le returneaza
            pe toate
            Returneaza o lista de obiecte Book
        '''
        ToSortList = []
        allBooks = self.__books_repo.getAllBooks()

        for book in allBooks:
            ToSortList.append(allBooks[book])

        ToSortList.sort(key=lambda book: book.getRentedTimes(), reverse=True)

        return ToSortList[:3]

    def getClientsWithRentedBooks(self, sortingType):
        '''
            sortingType - tipul de sortare
            Returneaza o lista cu toti clientii care au cel putin o carte inchiriata
        '''
        DasDictionar = {}  # Dict[idClient] = ClientBooksDTO
        AllRents = self.__rentals_repo.getAll()

        for rent in AllRents:
            idClientRent = AllRents[rent].getClientId()
            idBook = AllRents[rent].getBookId()
            if idClientRent in DasDictionar:
                DasDictionar[idClientRent].setNrBooks(DasDictionar[idClientRent].getNrBooks() + 1)
            else:
                DasDictionar[idClientRent] = ClientBooksDTO(self.__clients_repo.getClientById(idClientRent).getName())
                DasDictionar[idClientRent].setNrBooks(1)
                DasDictionar[idClientRent].addBook(self.__books_repo.getBookById(idBook).getTitle())

        FinalList = []

        for elem in DasDictionar:
            FinalList.append(DasDictionar[elem])

        if sortingType == 0:
            FinalList.sort(key=lambda dto: dto.getNameClient())
        elif sortingType == 1:
            FinalList.sort(key=lambda dto: -dto.getNrBooks())
        else:
            FinalList.sort(key=lambda dto: (dto.getNameClient(), -dto.getNrBooks()))

        return FinalList

    def getTopClients(self):
        '''
            Returneaza o lista cu primii 20% cei mai activi clienti
        '''
        DasList = self.getClientsWithRentedBooks(1)

        return DasList[:int(len(DasList)/5)]

    def getClientsWithoutBooks(self):
        ClientsList = self.__clients_repo.getAllClients()
        ToReturnList = []
        for client in ClientsList:
            if ClientsList[client].getRentedBooks() == 0:
                ToReturnList.append(ClientsList[client])

        return ToReturnList


