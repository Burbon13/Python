from Domain.Recipe import Recipe
from Domain.Medicine import Medicine

class PharmacyService:
    def __init__(self, medsRepo):
        self.__medsRepo = medsRepo

    def lookup(self, name):
        return self.__medsRepo.getByName(name)

    def create_recipe(self, list_entries):
        finalMeds = []

        for entry in list_entries:
            finalMeds.append(self.__medsRepo.getByName(entry))

        return Recipe(finalMeds)
