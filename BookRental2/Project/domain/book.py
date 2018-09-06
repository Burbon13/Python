class Book:
    def __init__(self, identity, title, author ,description):
        '''
        Create a new book with the given identity,title,description and author
        identity - int
        title,description,author - string
        '''
        self.__identity = identity
        self.__title = title
        self.__description = description
        self.__author = author
        self.__rentedTimes = 0
        self.__isRented = False

    def getIdentity(self):
        return self.__identity

    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getAuthor(self):
        return self.__author

    def getRentedTimes(self):
        return self.__rentedTimes

    def getIsRented(self):
        return self.__isRented

    def setIdentity(self, newidentity):
        self.__identity = newidentity

    def setTitle(self, newTitle):
        self.__title = newTitle

    def setDescription(self, newDescription):
        self.__description = newDescription

    def setAuthor(self, newAuthor):
        self.__author = newAuthor

    def setRentedTimes(self, rentedTimes):
        self.__rentedTimes = rentedTimes

    def setIsRented(self, isRented):
        self.__isRented = isRented
        if isRented == True:
            self.__rentedTimes = self.__rentedTimes + 1

    def initializeRented(self, isRented):
        self.__isRented = isRented

    def __eq__(self, st):
        '''
        Verify equality
        st - student
        return True if the curent student equals with st (have the same identity)
        '''
        return isinstance(st,self.__class__) and self.getIdentity() == st.getIdentity()

    def __str__(self):
        return "ID: " + str(self.getIdentity()) + " TITLU: " + self.getTitle() + " AUTOR: " + self.getAuthor() + " DESCR" \
                "IERE: " + self.getDescription() + " INCHIRIERI: " + str(self.getRentedTimes()) + " ESTE " + str(self.getIsRented())


