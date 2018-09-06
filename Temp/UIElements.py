def showMenu():
    print("Bine ai venit in aplicatia de banking management!")
    print("Comenzi:")
    print("0 - Exit")
    print("1 - Adaugare de noi tranzactii")
    print("3 - Cautari")


def getInteger(inputText):
    '''
    Citeste valoarea introdusa la tastatura. Cat timp valoarea nu este un numar, asteapta un nou input
    :param inputText(textul ce este afisat inainte de citire):
    :return: numarul citit
    '''
    while True:
        try:
            command = int(input(inputText))
            return command
        except ValueError:
            print("Valoarea introdusa nu este un numar valid. Reincercati!")


def getDate(text):
    '''
    Citeste trei numere care reprezinta anul,luna si ziua
    :param text:
    :return (ziua,luna,anul) touple cu data introdusa:
    '''
    print(text)
    year = getInteger("Introduceti anul:")
    month = getInteger("Introduceti luna:")
    day = getInteger("Introduceti ziua:")
    #se pot introduce teste de verificare daca data introdusa este valida

    return (day,month,year)


def printTransactions(transactionsList):
    for transaction in transactionsList:
        print(transaction[0], end = " ")
        print(transaction[1], end = " ")
        print(transaction[2])
