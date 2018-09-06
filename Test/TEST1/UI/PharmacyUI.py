from Repository.MedicineRepository import MedicineRepositoryException

class PharmacyUI:
    def __init__(self, pharmServ):
        self.__pharmServ = pharmServ

    def UIlookup(self, name):
        print(self.__pharmServ.lookup(name))

    def UIRetata(self, params):
        print(self.__pharmServ.create_recipe(params))

    def run(self):
        while True:
            command = input(">>")
            command = command.strip()
            command = command.split(',')


            if len(command) == 1 and command[0] == 'exit':
                print('La reverede')
                return

            if len(command) == 2 and command[0] == 'cauta':
                try:
                    self.UIlookup(command[1])
                except MedicineRepositoryException as mre:
                    print(mre)
            elif len(command) > 1 and command[0] == 'reteta':
                try:
                    self.UIRetata(command[1:])
                except MedicineRepositoryException as mre:
                    print(mre)
            else:
                print("Comanda invalida!")




