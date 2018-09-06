from domain.apartment import Apartment


class ApartmentRepoException(Exception):
    pass


class ApartmentRepo():
    def __init__(self, fileName):
        self.__listAp = []
        self.__fileName = fileName
        self.__loadFromFile()

    def __loadFromFile(self):
        file = open(self.__fileName, "r")

        for line in file:
            ap = line.split(',')
            self.__listAp.append(Apartment(int(ap[0]),ap[1],int(ap[2])))

        file.close()

    def findByNr(self, nr):
        for ap in self.__listAp:
            if ap.getNrAp() == nr:
                return ap

        raise ApartmentRepoException("Apartamentul nu exista in repo!")

    def getAll(self):
        return self.__listAp
