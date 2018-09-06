class Apartment:
    def __init__(self, nrAp, numeFam, nrLoc):
        self.__nrAp = nrAp
        self.__numeFam = numeFam
        self.__nrLoc = nrLoc

    def getNrAp(self):
        return self.__nrAp

    def getNumeFam(self):
        return self.__numeFam

    def getNrLoc(self):
        return self.__nrLoc

    def __eq__(self, other):
        return self.getNrAp() == other.getNrAp()

    def __str__(self):
        return "Nr. Ap: " + str(self.getNrAp()) + "; Nume: " + self.getNumeFam() + "; Nr loc: " + str(self.getNrLoc())
