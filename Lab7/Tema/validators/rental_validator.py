class RentalValidatorException(Exception):
    pass


class RentalValidator:
    @staticmethod
    def validateRental(rental,clients_repo,books_repo):
        '''
            Valideaza o inchiriere de carte
            Parametri:
            rental = inchirierea de validat
            clients_repo = repo-ul de carti
            books_repo = repo-ul de carti
        '''
        errors = ""

        if clients_repo.clientExistsInRepo(rental.getClientId()) == False:
            errors += "Clientul nu exista in repo!\n"

        if books_repo.bookExistsInRepo(rental.getBookId()) == False:
            errors += "Cartea nu exista in repo!\n"
        else:
            if books_repo.getBookById(rental.getBookId()).getIsRented() == True:
                errors += "Cartea este deja inchiriata!\n"

        if len(errors) > 0:
            raise RentalValidatorException(errors)
