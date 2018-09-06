from domain.Bill import Bill

class ApartmentService:
    def __init__(self, apRepo):
        self.__apRepo = apRepo

    def sortByFamilyName(self):
        aparts = self.__apRepo.getAll()

        aparts.sort(key=lambda Ap: Ap.getNumeFam())

        return aparts

    def plata(self, nrAp, water, gas, intrt):
        return Bill(nrAp, water, gas, intrt)

    def getFam(self, nr):
        return self.__apRepo.findByNr(nr)
