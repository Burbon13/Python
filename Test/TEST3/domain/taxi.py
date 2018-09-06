class Taxi:
    def __init__(self, id, adress, x, y):
        self.__id = id
        self.__adress = adress
        self.__y = y
        self.__x = x

    def __eq__(self, other):
        return self.getId() == other.getId()

    def getId(self):
        return self.__id

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getAdress(self):
        return self.__adress

    def __str__(self):
        return str(self.getId()) + " - " + self.__adress + " - " + str(self.getX()) + " - " + str(self.getY())
