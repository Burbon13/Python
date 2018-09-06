from UIElements import getDate
from UIElements import getInteger
from UIElements import printTransactions

def addNewTransaction(transactionsList):
    '''
    Adauga in program o noua tranzactie
    :return:
    '''
    transactionDate = getDate("Data tranzactiei")
    transactionAmount = getInteger("Introduceti suma tranzactiei:")
    transactionType = getInteger("Introduceti tipul tranzactiei (0-intrare/1-iesite):")

    transactionsList.append([transactionDate,transactionAmount,transactionType])


def biggerAmountSearch(transactionsList, lowerLimitAmount):
    pass


def biggerPreviousAmountSearch(transactionsList, lowerLimitAmount, dateLimit):
    pass


def oneTypeSearch(transactionsList, transactionsType):
    pass


def searchTransactionsCommand1(transactionsList):
    amountLimit = getInteger("Introduceti limita inferioara de bani.")
    biggerAmountSearch(transactionsList, amountLimit)


def searchTransactionsCommand2(transactionsList):
    amountLimit = getInteger("Introduceti limita inferioara de bani.")
    dateLimit = getDate("Introduceti data limita (se vor selecta tranzactiile anterioare)")
    biggerPreviousAmountSearch(transactionsList, amountLimit, dateLimit)


def searchTransactionsCommand3(transactionsList):
    transactionType = getInteger("Introduceti tipul tranzactiilor dorite.")
    oneTypeSearch(transactionsList,transactionsType)


def searchTransactions(transactionsList):
    '''
    Cauta tranzactii dupa anumite criterii
    :return:
    '''
    commandList = {1 : searchTransactionsCommand1, 2 : searchTransactionsCommand2, 3 : searchTransactionsCommand3}
    while True:
        command = getInteger("Introduce optiunea dorita:")
        if command == 0:
            print("Intoarcere la meniul principal.")
            return
        elif command in commandList:
            commandList[command]()
        else:
            print("Comanda invalida!")
