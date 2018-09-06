class ClientBooksDTO:
    def __init__(self, nameClient):
        self.__nameClient = nameClient
        self.__nrBooks = 0
        self.__books = []

    def getNameClient(self):
        return self.__nameClient

    def setNrBooks(self, nrBooks):
        self.__nrBooks = nrBooks

    def getNrBooks(self):
        return self.__nrBooks

    def addBook(self, book):
        self.__books.append(book)

    def __str__(self):
        return "NUME: " + str(self.__nameClient) + " CARTI INCHIRIATE: " + str(self.__nrBooks);

    def __eq__(self, other):
        return self.__nameClient == other.__nameClient
