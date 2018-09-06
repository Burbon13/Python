from Domain.Medicine import Medicine

class MedicineRepositoryException(Exception):
    pass

class MedicineRepository:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__meds = []
        self.__loadFromFile()

    def __loadFromFile(self):
        file = open(self.__fileName, "r")

        for line in file:
            strMed = line
            listDet = strMed.split(',')
            toAddMed = Medicine(listDet[0], float(listDet[1]))
            self.__meds.append(toAddMed)

        file.close()

    def getByName(self, name):

        for med in self.__meds:
            if med.getName() == name:
                return med

        raise MedicineRepositoryException("Nu exista in repo!")

    def getAll(self):
        return self.__meds
