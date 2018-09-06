from domain.client import Client

class ClientRepositoryException(Exception):
    pass


class ClientRepository:
    def __init__(self, fileName):
        '''
            Initializaeaza repo-ul de clienti cu un dictionar vid
        '''
        self.__clients = {}
        self.__fileName = fileName
        self.__loadFromFile()


    def __createClientFromLine(self, line):

        info = line.split("@")
        clToRETURN = Client(int(info[0]), info[1], int(info[2]))
        clToRETURN.setRentedBooks(int(info[3]))

        return clToRETURN

    def __loadFromFile(self):
        '''
            Load Books from file
        '''

        clientsFile = open(self.__fileName, "r+")

        try:
            for line in clientsFile:
                if line.strip() == "":
                    continue
                client = self.__createClientFromLine(line)
                self.__clients[client.getIdentity()] = client
        finally:
            clientsFile.close()

        '''with open(self.__fileName, "r+") as booksFile:
            for line in booksFile:
                if line.strip() == "":
                    continue
                book = self.__createBookFromLine(line)
                self.store(book)'''

    def __appendToFile(self, client):
        clientsFile = open(self.__fileName, "a+")

        try:
            line = str(client.getIdentity()) + "@" + client.getName() + "@" + str(client.getSsn()) + "@"\
                   + str(client.getRentedBooks()) + "\n"

            clientsFile.write(line)
        finally:
            clientsFile.close()

    def __storeToFile(self):
        clientsFile = open(self.__fileName, "w")

        try:
            for cl in self.__clients:
                client = self.__clients[cl]
                line = str(client.getIdentity()) + "@"
                line += client.getName() + "@" + str(client.getSsn()) + "@" + str(client.getRentedBooks()) + "\n"

                #print(line)

                clientsFile.write(line)

        finally:
            clientsFile.close()

    def save(self):
        self.__storeToFile()

    def store(self, client):
        '''
            Adauga un client in repo
            Parametri:
            client = clientul de adaugat
        '''
        if client.getIdentity() in self.__clients:
            raise ClientRepositoryException("Clientul de adaugat exista in repo deja!")

        self.__clients[client.getIdentity()] = client
        self.__appendToFile(client)

    def modify(self, client):
        '''
            Modifica un client din repo
            Parametri:
            client = clientul de modificat
        '''
        if client.getIdentity() not in self.__clients:
            raise ClientRepositoryException("Clientul de modificat nu exista in repo!")

        client.setRentedBooks(self.__clients[client.getIdentity()].getRentedBooks())

        self.__clients[client.getIdentity()] = client
        self.save()

    def delete(self, identity):
        '''
            Sterge un client din repo
            Parametri:
            identity = id-ul clientului de modificat
        '''
        if identity not in self.__clients:
            raise ClientRepositoryException("Clientul de sters nu exista in repo!")

        del self.__clients[identity]
        self.save()

    def size(self):
        '''
            Returneaza dimensiunea repo-ului (nr de clienti)
        '''
        return len(self.__clients)

    def getAllClients(self):
        '''
            Returneaza toti clientii
        '''
        return self.__clients

    def getClientById(self, identity):
        '''
            Returneaza clientul cu un anumit id
            Parametri:
            identity = id-ul clientului de cautat
            Return: clientul gasit cu id-ul identity
        '''
        if identity not in self.__clients:
            raise ClientRepositoryException("Clientul nu exista!")

        return self.__clients[identity]

    def clientExistsInRepo(self, idClient):
        '''
            Verifica daca un client exista in repo
            Returneaza:
            True - Daca exista
            False - in caz cotnrat
        '''
        return idClient in self.__clients
