class BookValidatorException(Exception):
    pass


class BookValidator:
    @staticmethod
    def validateBook(book):
        '''
            Functie de validare a unei carti, ridica eroare in cazul in care
            cartea nu este valida
            Parametri:
            book = cartea de validat
        '''
        errors = ""

        if book.getIdentity() <= 0:
            errors += "Identitatea cartii trebuie sa fie un numar natural strict pozitiv!\n"
        if len(book.getTitle()) == 0:
            errors += "Titlul cartii trebuie sa fie diferit de nul!\n"
        if len(book.getAuthor()) == 0:
            errors += "Autorul cartii trebuie sa fie diferit de nul!\n"

        if len(errors) > 0:
            raise BookValidatorException(errors)
