from domain.taxi import Taxi


class TaxiRepoException(Exception):
    pass

class TaxiRepo:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__taxis = []
        self.__loadFromFile()

    def __loadFromFile(self):
        file = open(self.__fileName, "r")

        for line in file:
            taxi_line = line.split(",")
            newTaxi = Taxi(int(taxi_line[0]),taxi_line[1],int(taxi_line[2]),int(taxi_line[3]))
            self.__taxis.append(newTaxi)

        file.close()

    def store(self):
        file = open(self.__fileName, "w")

        for taxi in self.__taxis:
            file.write(str(taxi.getId())+','+taxi.getAdress()+','+str(taxi.getX())+','+str(taxi.getY())+'\n')

        file.close()

    def modify(self, id, adress, x, y):
        for i in range(len(self.__taxis)):
            if self.__taxis[i].getId() == id:
                del self.__taxis[i]
                self.__taxis.append(Taxi(id,adress,x,y))
                self.store()
                return

        raise TaxiRepoException("Taxiul nu exista in repo!")

    def getAll(self):
        return self.__taxis
