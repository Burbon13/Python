from repository.client_repo import ClientRepositoryException
from repository.book_repo import BookRepositoryException
from repository.rentals_repo import RentalsException
from validators.client_validator import ClientValidatorException
from validators.book_validator import BookValidatorException
from validators.rental_validator import RentalValidatorException
from domain.clint_with_booksDTO import ClientBooksDTO
from ui.texts import instructions


class Console:
    def __init__(self, book_service, client_service, rental_service):
        '''
            Functia de initializare a consolei
            Parametri: controller - controller-ul aplicatiei
        '''
        self.__book_service = book_service
        self.__client_service = client_service
        self.__rental_service = rental_service

    def __createInstruction(self, string):
        '''
             Separa stringul in functie de virgule si elimina
             spatiile de la inceput si final, returneaza lista
             cu elementele gasite
             string - stringul pe care se lucreaza
             Return: lista parametrilor functiei
        '''
        aux_list = string.split(',')
        final_list = []
        for par in aux_list:
            final_list.append((par.lstrip()).rstrip())
        return final_list

    def __uiAddBook(self, params):  # numele si descrierea sunt mai greu de adaugat
        '''
            Functie de adaugare de carte
            Parametri: params = lista[identity:,title,author,description]
            Returneaza un string de confirmare a finalizarii functiei
        '''
        if len(params) != 4:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        title = params[1]
        author = params[2]
        description = params[3]
        self.__book_service.addBook(identity, title, author, description)

        return "Cartea a fost adaugata cu succes!"

    def __uiDeleteBook(self, params):
        '''
            Functie de stergere de carte
            Parametri: params=lista[identity]
            Returneaza un string de confirmare a finalizarii functiei
        '''
        if len(params) != 1:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        self.__book_service.deleteBook(identity)

        return "Cartea a fost stearsa cu succes"

    def __uiModifyBook(self, params):
        '''
            Functie de modificare de carte
            Parametri: params=lista[identity:,title,author,description]
            Returneaza un string de confirmare a finalizarii functiei
        '''
        if len(params) != 4:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        title = params[1]
        author = params[2]
        description = params[3]
        self.__book_service.modifyBook(identity, title, author, description)

        return "Cartea a fost modificata cu succes!"

    def __printAllBooks(self, params):
        '''
            Afiseaza cartile din repo
            Parametri: params = lista goala
            Returneaza stringul vid
        '''
        if len(params) != 0:
            return "Numar invalid de parametri!"

        books = self.__book_service.getAllBooks()

        if len(books) == 0:
            return "Nu exista carti!"

        for book in books:
            print(books[book])

        return ""

    def __uiAddClient(self, params):
        '''
            Functie de adaugare de client
            Parametri: params = lista[identity,name,ssn]
            Returneaza un string de confirmare a finalizarii functiei
        '''
        if len(params) != 3:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        name = params[1]
        ssn = int(params[2])
        self.__client_service.addClient(identity, name, ssn)

        return "Clientul a fost adaugat cu succes!"

    def __uiDeleteClient(self, params):
        '''
            Functie de stergere client
            Parametri: params = lista[identity]
            Returneaza un string de confirmare a finalizarii functiei
        '''
        if len(params) != 1:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        self.__client_service.deleteClient(identity)

        return "Clientul a fost stears cu succes!"

    def __uiModifyClient(self, params):
        '''
            Functie de adaugare de client
            Parametri: params = lista[identity,name,ssn]
            Returneaza un string de confirmare a finalizarii functiei
        '''
        if len(params) != 3:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        name = params[1]
        ssn = int(params[2])
        self.__client_service.modifyClient(identity, name, ssn)

        return "Clientul a fost modificat cu succes!"

    def __printAllClients(self, params):
        '''
            Afiseaza clientii din repo
            Parametri: params = lista goala
            Returneaza stringul vid
        '''
        if len(params) != 0:
            return "Numar invalid de parametri!"

        clients = self.__client_service.getAllClients()
        if len(clients) == 0:
            return "Nu exista clienti!"
        for client in clients:
            print(clients[client])

        return ""

    def __uiSearchClient(self, params):
        '''
            Cauta client in functie de id
            params = list [identity]
            Returneaza stringul vid
        '''
        if len(params) != 1:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        client = self.__client_service.getClient(identity)
        print(client)

        return ""

    def __uiSearchBook(self, params):
        '''
            Cauta carte in functie de id
            params = list [identity]
            Returneaza stringul vid
        '''
        if len(params) != 1:
            return "Numar invalid de parametri!"

        identity = int(params[0])
        book = self.__book_service.getBook(identity)
        print(book)

        return ""

    def __uiRentBook(self, params):
        '''
            Adauga o inchiriere de carte
            Parametri:
            params = lista[idCarte,idClient]
            Returneaza: string de validare a inchirierii
        '''
        if len(params) != 2:
            return "Numar invalid de parametri!"

        idClient = int(params[0])
        idBook = int(params[1])

        self.__rental_service.rentBook(idClient, idBook)

        return "Cartea a fost inchiriata cu succes!"

    def __uiReturnBook(self, params):
        '''
            Returneaza o carte carte de catre un client
            Parametri:
            params = lista[idCarte,idClient]
            Returneaza: string de validare a returnarii cartii
        '''
        if len(params) != 2:
            return "Numar invalid de parametri!"

        idClient = int(params[0])
        idBook = int(params[1])

        self.__rental_service.returnBook(idClient, idBook)

        return "Cartea a fost returnata cu succes!"

    '''
    def __printList(self, pList):
        for element in pList:
            print(element)
    '''

    # --------------RECURSIVE TASK 1---------------------
    def __printList(self, pList):
        if len(pList) == 0:
            return
        print(pList[0])
        self.__printList(pList[1:])

    # --------------RECURSIVE TASK 1---------------------

    def __printAllRentals(self, params):
        '''
            Afiseaza toate inchirierile de carti
            params - lista vida
        '''
        if len(params) != 0:
            return "Numar invalid de parametri!"

        rentals = self.__rental_service.getAllRentals()

        if len(rentals) == 0:
            return "Nu exista carti inchiriate!"

            # for rent in rentals:
            # print(rentals[rent])

        self.__printList(rentals)

        return ""

    def __uiTopRentedBooks(self, params):
        '''
            Afiseaza primele 3 cele mai inchiriate carti
        '''
        if len(params) != 0:
            return "Numar invalid de parametri!"

        topBooks = self.__rental_service.getMostRentedBooks()

        if len(topBooks) == 0:
            return "Nu exista carti!"

            # for top in topBooks:
            # print(top)

        self.__printList(topBooks)

        return ""

    def __uiGetClientsWithBooks(self, params):
        '''
            Afiseaza clientii care au cart inchiriate
        '''
        if len(params) != 1:
            return "Numar invalid de parametri!"

        if params[0] == "nume":
            dasClients = self.__rental_service.getClientsWithRentedBooks(0)
        elif params[0] == "numar":
            dasClients = self.__rental_service.getClientsWithRentedBooks(1)
        elif params[0] == "ambele":
            dasClients = self.__rental_service.getClientsWithRentedBooks(2)
        else:
            return "Parametru invalid!"

        if len(dasClients) == 0:
            return "Nu exista clienti!"

            # for client in dasClients:
            # print(client)

        self.__printList(dasClients)

        return ""

    def __uigetFirstTwentyPrecentClients(self, params):
        '''
            Functie care ne afiseaza topul clientilor
        '''
        if len(params) != 0:
            return "Numar invalid de parametri!"

        topClients = self.__rental_service.getTopClients()

        if len(topClients) == 0:
            return "Nu exista clienti!"

            # for top in topClients:
            # print(top)

        self.__printList(topClients)

        return ""

    def __uiNewRaport(self, params):
        '''
            Afiseaza clientii care nu au carti inchriate
        '''
        if len(params) != 0:
            return "Numar invalid de parametri!"

        badClients = self.__rental_service.getClientsWithoutBooks()

        if len(badClients) == 0:
            print("Nu exista clienti fara o carte inchiriata!")

            # for client in badClients:
            # print(client)

        self.__printList(badClients)

        return ""

    def run(self):
        '''
            Functia principala a controlerului care asteapta
            comenzi de la user
        '''
        command_list = {"adauga.carte": self.__uiAddBook, "sterge.carte": self.__uiDeleteBook,
                        "modifica.carte": self.__uiModifyBook, "adauga.client": self.__uiAddClient,
                        "sterge.client": self.__uiDeleteClient, "modifica.client": self.__uiModifyClient,
                        "afis.carti": self.__printAllBooks, "afis.clienti": self.__printAllClients,
                        "cauta.client": self.__uiSearchClient, "cauta.carte": self.__uiSearchBook,
                        "inchiriere.carte": self.__uiRentBook, "returnare.carte": self.__uiReturnBook,
                        "afis.inchirieri": self.__printAllRentals, "top.inchiriate": self.__uiTopRentedBooks,
                        "clienti.cu.carti": self.__uiGetClientsWithBooks,
                        "top.clienti": self.__uigetFirstTwentyPrecentClients,
                        "raport.nou": self.__uiNewRaport}

        while True:
            command = self.__createInstruction(input(">>"))

            if len(command) == 0:
                continue
            if command[0] == "exit" and len(command) == 1:
                print("La reverede!")
                return
            if command[0] == "help" and len(command) == 1:
                print(instructions)
                continue

            if command[0] in command_list:
                try:
                    function_result = command_list[command[0]](command[1:])
                    if function_result != "":
                        print(function_result)
                except BookRepositoryException as bre:
                    print(str(bre))
                except ClientRepositoryException as cre:
                    print(str(cre))
                except BookValidatorException as bve:
                    print(str(bve))
                except ClientValidatorException as cve:
                    print(str(cve))
                except RentalsException as re:
                    print(str(re))
                except RentalValidatorException as rve:
                    print(str(rve))
                except ValueError:
                    print("ID-ul si CNP-ul trebuie sa fie valori intregi si pozitive!")
                except FileNotFoundError as fnfe:
                    print(str(fnfe))

            else:
                print("Comanda invalida!")
