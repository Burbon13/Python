from repo.ApartmentRepo import ApartmentRepoException

class Console:
    def __init__(self, serviceAp):
        self.__serviceAp = serviceAp

    def __uiSorted(self):
        theList = self.__serviceAp.sortByFamilyName()

        for ap in theList:
            print(ap)

    def __uiPlata(self, params):
        bil = self.__serviceAp.plata(int(params[0]),int(params[1]),int(params[2]),int(params[3]))

        print(self.__serviceAp.getFam(int(params[0])))
        print(bil)

    def run(self):
        while True:
            command = input(">>")
            command = command.split(',')

            if len(command) == 1 and command[0] == 'exit':
                print("Salut!")
                return

            try:
                if len(command) == 1 and command[0] == 'sortate':
                    self.__uiSorted()
                    continue

                if len(command) == 5 and command[0] == 'plata':
                    self.__uiPlata(command[1:])
                    continue
            except ApartmentRepoException as are:
                print(are)

            print("Comanda invalida!")
