from repo.taxi_repo import TaxiRepoException

class ConsoleUI:
    def __init__(self, service):
        self.__service = service

    def __setTaxiUI(self, params):
        self.__service.modifyTaxi(int(params[0]),params[1],int(params[2]),int(params[3]))

    def __getByAdress(self, adress):
        toPrint = self.__service.getFromAdress(adress)

        for i in toPrint:
            print(i)

    def __sortare(self, x, y):
        x = int(x)
        y = int(y)

        toPrint = self.__service.orderByDistance(x,y)

        for i in toPrint:
            print(i)

    def run(self):
        while True:
            command = input(">>")

            command = command.split(',')

            try:
                if len(command) == 1 and command[0] == 'exit':
                    print("Salutare!")
                    return

                if len(command) == 5 and command[0] == 'set':
                    self.__setTaxiUI(command[1:])
                    print("Schimbare efectuata cu succes!")
                    continue

                if len(command) == 2 and command[0] == 'adresa':
                    self.__getByAdress(command[1])
                    continue

                if len(command) == 3 and command[0] == 'punct':
                    self.__sortare(command[1],command[2])
                    continue

                print("Comanda invalida!")
            except TaxiRepoException as rpe:
                print(str(rpe))
            except ValueError:
                print("Trebuie intregi valorile!")