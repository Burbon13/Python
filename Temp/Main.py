from TransactionsOperations import addNewTransaction
from TransactionsOperations import searchTransactions
from UIElements import getInteger
from UIElements import showMenu


def run():
    '''
    Functia principala care este rulata pentru a porni programul
    :return:
    '''
    commandsList = {1 : addNewTransaction, 3 : searchTransactions}
    transactionsList = []
    showMenu()
    while True:
        command = getInteger("Introduceti comanda")
        if command == 0:
            print("La revedere!")
            return
        elif command in commandsList:
            commandsList[command](transactionsList)
        else:
            print("Comanda invalida!")


run()