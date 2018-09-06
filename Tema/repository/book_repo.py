from domain.book import Book


class BookRepositoryException(Exception):
    pass


class BookRepository:
    def __init__(self, fileName):
        self.__books = {}
        self.__fileName = fileName
        self.__loadFromFile()

    def __createBookFromLine(self, line):

        info = line.split("@")
        bkToRETURN = Book(int(info[0]), info[1], info[2], info[3])
        bkToRETURN.setRentedTimes(int(info[4]))
        if int(info[5]) == 0:
            bkToRETURN.initializeRented(False)
        else:
            bkToRETURN.initializeRented(True)

        return bkToRETURN

    def __loadFromFile(self):
        '''
            Load Books from file
        '''

        booksFile = open(self.__fileName, "r+")

        try:
            for line in booksFile:
                if line.strip() == "":
                    continue
                book = self.__createBookFromLine(line)
                self.__books[book.getIdentity()] = book
        finally:
            booksFile.close()

        '''with open(self.__fileName, "r+") as booksFile:
            for line in booksFile:
                if line.strip() == "":
                    continue
                book = self.__createBookFromLine(line)
                self.store(book)'''

    def __appendToFile(self, book):
        booksFile = open(self.__fileName, "a+")

        try:
            line = str(book.getIdentity()) + "@" + book.getTitle() + "@" + book.getAuthor() + "@" + book.getDescription() +\
                 "@" + str(book.getRentedTimes()) + "@"

            if book.getIsRented() == True:
                line += "1"
            else:
                line += "0"

            line += "\n"

            booksFile.write(line)
        finally:
            booksFile.close()

    def __storeToFile(self):
        booksFile = open(self.__fileName, "w")

        try:
            for bk in self.__books:
                book = self.__books[bk]
                line = str(book.getIdentity()) + "@" + book.getTitle() + "@" + book.getAuthor() + "@" + book.getDescription() + \
                     "@" + str(book.getRentedTimes()) + "@"

                if book.getIsRented() == True:
                    line += "1"
                else:
                    line += "0"

                line += "\n"

                booksFile.write(line)

        finally:
            booksFile.close()

    def save(self):
        self.__storeToFile()

    def store(self, book):
        '''
            Adauga o carte in repo
            Parametri:
            book = cartea de adaugat
        '''
        if book.getIdentity() in self.__books:
            raise BookRepositoryException("Cartea de adaugat exista in repo deja!")

        self.__books[book.getIdentity()] = book
        self.__appendToFile(book)

    def modify(self, book):
        '''
            Modifica o carte in repo
            Parametri:
            book - cartea de modificat
        '''
        if book.getIdentity() not in self.__books:
            raise BookRepositoryException("Cartea de modificat nu exista in repo!")

        isRented = self.__books[book.getIdentity()].getIsRented()
        rentedTimes = self.__books[book.getIdentity()].getRentedTimes()

        self.__books[book.getIdentity()] = book
        self.__books[book.getIdentity()].setIsRented(isRented)
        self.__books[book.getIdentity()].setRentedTimes(rentedTimes)

        self.__storeToFile()

    def delete(self, identity):
        '''
            Sterge o carte din repo
            Parametri:
            identity = id-ul cartii de sters
        '''
        if identity not in self.__books:
            raise BookRepositoryException("Cartea de sters nu exista in repo!")

        del self.__books[identity]

        self.__storeToFile()

    def size(self):
        '''
            Returneaza dimensiunea repo-ului
        '''
        return len(self.__books)

    def getAllBooks(self):
        '''
            Returneaza toate cartile din repo
        '''
        return self.__books

    def getBookById(self, identity):
        '''
            Cauta carte in repo un functie de id
            Parametri:
            identity = id-ul cartii de cautat
        '''
        if identity not in self.__books:
            raise BookRepositoryException("Cartea nu exista!")

        return self.__books[identity]

    def bookExistsInRepo(self, idBook):
        '''
            Verifica daca un client exista in repo
            Returneaza:
            True - Daca exista
            False - in caz cotnrat
        '''
        return idBook in self.__books

