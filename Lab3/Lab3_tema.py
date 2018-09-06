from FindList import findListWithPrimes
from FindList import findListBetweenBounds


def showMenu():
    '''
    Afiseazaz un mesaj de inceput in care sunt enuntate comenzile disponibile
    '''
    print("Bine ai venit! Introduceti comanda dorita!\n" +
           "Comanda 0 - Iesirea din program\n" +
           "Comanda 1 - Citirea unei liste cu n elemente intregi\n" +
           "Comanda 2 - Gasirea unei secvente maximale cu elemente pare\n" +
           "Comanda 3 - Gasirea unei secvente maximale cu elemente cuprinse intre 0 si 10")


def readInt(text):
    '''
    Asteapta input si verifica daca este numar intreg
    Daca este il returneaza
    In caz contrat cere reintroducerea valorii
    '''
    while True:
        try:
            command = int(input(text))
            return command
        except ValueError:
            print("Valoare invalida")


def readList(my_list):
    '''
    Primeste parametru o lista pe care o curata
    Apoi citeste lungimea sirului si elementele sale pe care le adauga in sir
    '''
    my_list.clear()
    list_size = readInt("Introduceti marimea lista: ")
    for index in range(list_size):
        my_list.append(readInt("Introduceti elementul %d: " % (index + 1)))


def command1(my_list):
    '''
    Comanda 1 a consolei
    '''
    readList(my_list)


def command2(my_list):
    '''
    comanda 2 a consolei
    '''
    _list = findListWithPrimes(my_list)
    printList(_list)


def getBounds():
    '''
    Functia asteapta input pana primeste o pereche de numere
    cu conditia ca primul numar sa fie mai mic sau egal decat al doilea
    Input: 2 numere de la tastatura
    Output: touple cu 2 elemente
    '''
    while True:
        lower_bound = readInt("Introduceti limita inferioara: ")
        upper_bound = readInt("Introduceti limita superioasa: ")
        if upper_bound >= lower_bound:
            return (lower_bound,upper_bound)
        print("Nu exista interval cu valorile introduse!Reintroduceti valorile!")


def command3(my_list):
    '''
    comanda 3 a consolei
    '''
    bounds = getBounds()
    _list = findListBetweenBounds(my_list, bounds[0], bounds[1])
    printList(_list)


def printList(my_list):
    '''
    Afiseaza lista
    In cazul in care lista este vida, se afiseaza un mesaj corespunzator1
    '''
    if my_list == []:
        print("Lista este vida!")
    else:
        print(my_list)


def run():
    showMenu()
    my_list = []
    commandList = {1 : command1, 2 : command2, 3 : command3}
    while True:
        command = readInt("Introduceti comanda: ")
        if command == 0:
            print("La revedere!")
            return
        elif command in commandList:
            commandList[command](my_list)
        else:
            print("Comanda invalida!")

run()

