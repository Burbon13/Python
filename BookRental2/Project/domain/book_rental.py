class BookRental:
    def __init__(self, clientId, bookId):
        '''
            Initializeaza o inchiriere de carte
            Parametri: clientId = val intreg, id-ul clientului
                       bookId = val intreg, id-ul cartii
        '''
        self.__clientId = clientId
        self.__bookId = bookId

    def __eq__(self, other): #Trebuie verificat ca other sa fie instanta de self!!!!!!!!!!!!!!!!!
        '''
            Compara 2 inchirieri in functie de id
            Parametri: other - o alta instanta de inchiriere
            Returneaza: True - id-urile sunt egale , False - caz contrat
        '''
        return isinstance(other,self.__class__) and self.__clientId == other.__clientId and self.__bookId == other.__bookId

    def __str__(self):
        '''
            Returneaza un string mai estetic pentru a putea afisa o inchiriere
        '''
        return "Carte ID: " + str(self.__bookId) + "; Client ID: " + str(self.__clientId)

    def __hash__(self):
        id1 = self.__bookId
        id2 = self.__clientId
        return int(((id1+id2)*(id1+id2+1)) / 2 + id2)#aici ai ramas, nu erai sigur de aceasta functie hash tho :))

    def getClientId(self):
        '''
            Returneaza id-ul clientului
        '''
        return self.__clientId

    def getBookId(self):
        '''
            Returneaza id-ul cartii
        '''
        return self.__bookId

    def setClientId(self, identity):
        '''
            Seteaza id-ul clientului
            Parametri: identity - noul id de setat, valoare naturala pozitiva
        '''
        self.__clientId = identity

    def setBookId(self, identity):
        '''
            Seteaza id-ul cartii
            Parametri: identity - noul id de setat, valoare naturala pozitiva
        '''
        self.__bookId = identity