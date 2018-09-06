class Client:
    def __init__(self, identity, name, ssn): #ssn - social security number
        '''
        Create a new client with the given identity, name and social security number
        identity - int
        title,description,author - string
        '''
        self.__identity = identity
        self.__name = name
        self.__ssn = ssn
        self.__rentedBooks = 0

    def getIdentity(self):
        '''
            Returneaza identitatea instantei curente
        '''
        return self.__identity

    def getName(self):
        '''
            Returneaza numele instantei curente
        '''
        return self.__name

    def getSsn(self):
        '''
            Returneaza CNP-ul instantei curente
        '''
        return self.__ssn

    def getRentedBooks(self):
        return self.__rentedBooks

    def setRentedBooks(self, rentedBooks):
        self.__rentedBooks = rentedBooks

    '''def setIdentity(self, identity):
        
            Seteaza identitatea instantei curente 
        
        self.__identity = identity'''

    def setName(self, name):
        '''
            Seteaza numele instantei curente
            Parametri:
            name = numele, string
        '''
        self.__name = name

    def setSsn(self, ssn):
        '''
            Seteaza CNP-ul instantei curente
            Parametri:
            ssn = CNP, nr nat cu nr fixat de cifre
        '''
        self.__ssn = ssn

    def __eq__(self, cl):
        '''
        Verify equality
        st - student
        return True if the curent student equals with st (have the same identity)
        '''
        return isinstance(cl,self.__class__) and self.getIdentity() == cl.getIdentity()

    def __str__(self):
        return "ID: " + str(self.getIdentity()) + " NUME: " + self.getName() + " CNP: " + str(self.getSsn()) + " BOOKS RENTED: " + str(self.getRentedBooks())