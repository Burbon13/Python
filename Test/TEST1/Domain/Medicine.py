class Medicine:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def __str__(self):
        return self.__name + " - " + str(self.__price) + " lei"

    def __eq__(self, other):
        return self.getName() == other.getName()
