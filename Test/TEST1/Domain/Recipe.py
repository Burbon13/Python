class Recipe:
    def __init__(self, listRetete):
        self.__listRetete = listRetete

    def getTotalSum(self):
        sumTotal = 0

        for reteta in self.__listRetete:
            sumTotal = sumTotal + reteta.getPrice()

        return sumTotal

    def __str__(self):
        strAf = ""

        for reteta in self.__listRetete:
            strAf += str(reteta)
            strAf += "\n"

        strAf += "Cost: " + str(self.getTotalSum()) + "\n"

        return strAf