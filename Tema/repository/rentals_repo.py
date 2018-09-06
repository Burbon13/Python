from domain.book_rental import BookRental

class RentalsException(Exception):
    pass


class Rentals:
    def __init__(self, fileName):
        '''
            Initializeaza repo-ul de inchirieri cu un dictionar vid
        '''
        self.__rentals = {}
        self.__fileName = fileName
        self.__loadFromFile()

    def __createRentalFromLine(self, line):

        info = line.split("@")
        brToRETURN = BookRental(int(info[0]), int(info[1]))

        return brToRETURN

    def __loadFromFile(self):
        '''
            Load Rentals from file
        '''

        brFile = open(self.__fileName, "r+")

        try:
            for line in brFile:
                if line.strip() == "":
                    continue
                rental = self.__createRentalFromLine(line)
                self.__rentals[rental] = rental
        finally:
            brFile.close()

        '''with open(self.__fileName, "r+") as booksFile:
            for line in booksFile:
                if line.strip() == "":
                    continue
                book = self.__createBookFromLine(line)
                self.store(book)'''

    def __appendToFile(self, rental):
        brFile = open(self.__fileName, "a+")

        try:
            line = str(rental.getClientId()) + "@" + str(rental.getBookId()) + "\n"

            brFile.write(line)
        finally:
            brFile.close()

    def __storeToFile(self):
        brFile = open(self.__fileName, "w")

        try:
            for rt in self.__rentals:
                rental = self.__rentals[rt]
                line = str(rental.getClientId()) + "@" + str(rental.getBookId()) + "\n"

                #print(line)

                brFile.write(line)

        finally:
            brFile.close()

    def save(self):
        self.__storeToFile()

    #-------------------------

    def store(self, bookRental):
        '''
            Adauga o inchiriere de carte in repo
            Parametri:
            clientId = id-ul clientului care inchiriaza, valoare naturala pozitiva
            bookId = id-ul cartii de inchiriat, valoare naturala pozitiva
        '''
        if bookRental in self.__rentals:
            raise RentalsException("Inchirierea exista deja in repo!")

        self.__rentals[bookRental] = bookRental
        self.__appendToFile(bookRental)

    def delete(self, rental):
        '''
            Sterge o inchiriere de carte
            Parametri:
            rental = inchirierea de sters
        '''
        if rental not in self.__rentals:
            raise RentalsException("Inchirierea de sters nu exista in repo!")

        del self.__rentals[rental]
        self.save()

    def modifyClient(self, rental, newClientId):
        '''
            Modifica clientul
            Parametri:
            newClientId = noul id care va fi asociat inchirierii
        '''
        if rental not in self.__rentals:
            raise RentalsException("Inchirierea de sters nu exista in repo!")

        rental.setClientId(newClientId)
        self.save()

    def modifyBook(self, rental, newBookId):
        '''
            Modifica cartea
            Parametri:
            newBookId = noul id care va fi asociat cartii
        '''
        if rental not in self.__rentals:
            raise RentalsException("Inchirierea de sters nu exista in repo!")

        rental.setBookId(newBookId)
        self.save()

    def getAll(self):
        return self.__rentals

