class ClientValidatorException(Exception):
    pass


class ClientValidator:
    @staticmethod
    def validateClient(client):
        '''
            Verifica daca un client este valid. In cazul in care nu este,
            ridica o exceptie.
            Parametri:
            client = clientul de validat
        '''
        errors = ""

        if client.getIdentity() <= 0:
            errors += "Identitatea clientului trebuie sa fie un numar natural stict pozitiv!\n"
        if len(client.getName()) == 0:
            errors += "Numele clientului trebuie sa fie diferit de nul!\n"
        if 1000000000000 > client.getSsn() or client.getSsn() >= 10000000000000:
            errors += "CNP invalid!\n"

        if len(errors) > 0:
            raise ClientValidatorException(errors)
