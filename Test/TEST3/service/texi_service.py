class TaxiService:
    def __init__(self, repoTaxi):
        self.__repoTaxi = repoTaxi

    def modifyTaxi(self, id, adress, x, y):
        self.__repoTaxi.modify(id,adress,x,y)

    def getFromAdress(self, adress):
        whole = self.__repoTaxi.getAll()
        toReturn = []

        for i in whole:
            if i.getAdress() == adress:
                toReturn.append(i)

        return toReturn

    def orderByDistance(self, x, y):
        whole = self.__repoTaxi.getAll()

        whole.sort(key=lambda this : (this.getX() - x)*(this.getX() - x) + (this.getY() - y) * (this.getY() - y))

        return whole
