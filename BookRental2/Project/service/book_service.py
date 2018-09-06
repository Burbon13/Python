from domain.book import Book

class BookServiceException(Exception):
    pass

class BookService:
    def __init__(self, books_repo, book_validator):
        self.__books_repo = books_repo
        self.__book_validator = book_validator

    def addBook(self, identity, title, author, description):
        '''
            Adauga o carte in repo
            Parametri:
            identity = identitatea cartii, valoare naturala pozitiva
            title = titlul cartii, string
            author = autorul cartii, string
            description = descrierea cartii, string
        '''
        new_book = Book(identity, title, author, description)
        self.__book_validator.validateBook(new_book)
        self.__books_repo.store(new_book)

    def deleteBook(self, identity):
        '''
            Sterge o carte din repo
            params:
            identity = id-ul cartii, valoare naturala pozitiva
        '''
        self.__books_repo.delete(identity)

    def modifyBook(self, identity, title, author, description):
        '''
            Modifica o carte in repo
            Parametri:
            identity = identitatea cartii, valoare naturala pozitiva
            title = titlul cartii, string
            author = autorul cartii, string
            description = descrierea cartii, string
        '''
        new_book = Book(identity, title, author, description)
        self.__book_validator.validateBook(new_book)
        self.__books_repo.modify(new_book)
        self.__books_repo.save()

    def getAllBooks(self):
        '''
            Returneaza toate cartile
        '''
        return self.__books_repo.getAllBooks()

    def getBook(self, id):
        return self.__books_repo.getBookById(id)
