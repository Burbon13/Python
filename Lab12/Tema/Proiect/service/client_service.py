from domain.client import Client

class ClientServiceException(Exception):
    pass

class ClientService:
    def __init__(self, clients_repo, client_validator):
        self.__clients_repo = clients_repo
        self.__clients_validator = client_validator

    def addClient(self, identity, name, ssn):
        '''
            Adauga un client in repo
            Parametri:
            identity = identitatea clientului, valoare naturala pozitiva
            name = numele clientului, string
            ssn = CNP-ul clientului, numar intreg de lungime fixata
        '''
        new_client = Client(identity,name,ssn)
        self.__clients_validator.validateClient(new_client)
        self.__clients_repo.store(new_client)

    def deleteClient(self, identity):
        '''
            Sterge un client din repo
            Parametri:
            identity = identitatea clientului, valoare naturala pozitiva
        '''
        self.__clients_repo.delete(identity)

    def modifyClient(self, identity, name, ssn):
        '''
            Modifica un client in repo
            Parametri:
            identity = identitatea clientului, valoare naturala pozitiva
            name = numele clientului, string
            ssn = CNP-ul clientului, numar intreg de lungime fixata
        '''
        new_client = Client(identity,name,ssn)
        self.__clients_validator.validateClient(new_client)
        self.__clients_repo.modify(new_client)
        self.__clients_repo.save()

    def getAllClients(self):
        '''
            Returneaza toti clientii din repo
        '''
        return self.__clients_repo.getAllClients()

    def getClient(self, id):
        return self.__clients_repo.getClientById(id)