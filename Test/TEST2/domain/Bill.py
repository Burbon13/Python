class Bill:
    def __init__(self, apartment, water, gas, intret):
        self.__apartment = apartment
        self.__water = water
        self.__gas = gas
        self.__intret = intret

    def getApartment(self):
        return self.__apartment

    def getWater(self):
        return self.__water

    def getGas(self):
        return self.__gas

    def getIntret(self):
        return self.__intret

    def getSumTotal(self):
        return 5 * self.__water + 10 * self.__gas + self.__intret

    def __str__(self):
        return  "Cost: " + str(self.getSumTotal())

