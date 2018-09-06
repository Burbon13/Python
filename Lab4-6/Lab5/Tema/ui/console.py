'''
    Interfata aplicatiei
'''

from domain.transactions import addNewTransaction
from domain.transactions import changeTransaction
from domain.transactions import getTransactions
from domain.transactions import deleteTransactionsFromDay
from domain.transactions import deleteTransactionsBetweenDays
from domain.transactions import deleteTransactionsOfType
from domain.transactions import searchTransactionsByAmount
from domain.transactions import searchTransactionsByAmountAndDate
from domain.transactions import searchTransactionsByType
from domain.transactions import searchAmountOneTypeTransactions
from domain.transactions import searchAmountAtTime
from domain.transactions import searchTransactionsByTypeSorted
from domain.transactions import filterByTypeAndSumTransactions
from domain.transactions import undo
from domain.utils import createTransaction
from domain.utils import createDataBase
from ui.texts import *


def run():
    '''
        Ruleaza meniul si asteapta comanda
    '''
    data = createDataBase()
    functionalities = {'adaugare' : addTransactionUI, 'cautare' : searchTransactionsUI,
                       'stergere' : deleteTransactionsUI, 'raport' : reportsUI,
                       'afisare' : printAllTransactionsUI, 'filtrare' : filterTransactionsUI,
                       'undo' : undoUI}
    #functionalities = {'1': addTransactionUI, '2': searchTransactionsUI,
    #                   '3': deleteTransactionsUI, '4': reportsUI,
    #                   '5': printAllTransactionsUI, '6': filterTransactionsUI,
    #                   '7': undoUI}
    print(instructions_list, end='\n\n')
    while True:
        command = input('Meniu PRINCIPAL. Introduce comanda: ')

        if command == 'exit':
            print('La revedere!')
            return
        elif command == 'help':
            print(instructions_list)
        elif command in functionalities:
            while True:
                try:
                    functionalities[command](data)
                    break
                except ValueError as ve:
                    print(ve)
        else:
            print('Comanda incorecta!\n')


def inputTransaction(text):
    '''
         Citeste o tranzactie
         text - string de afisar
         return dictionar cu tranzactia {ziua,suma,tip}
    '''
    print(text)
    day = input('Ziua: ')
    amount = input('Suma: ')
    ttype = input('Type: ')
    return createTransaction(day,amount,ttype)


def printTransactionsUI(transactions):
    '''
        Afiseaza tranzactiile dintr-o lista
        transactions - lista de tranzactii
    '''
    if len(transactions) == 0:
        print('Nu exista nicio tranzactie!\n')
        return

    for trans in transactions:
        print('Ziua: %d  Suma: %d  Tipul: %d' % (trans['day'], trans['amount'], trans['ttype']))


def printAllTransactionsUI(data):
    '''
        Afiseaza toate tranzactiile
    '''
    printTransactionsUI(getTransactions(data))


def addNewTransactionUI(data):
    '''
        Citeste de la tastatura si incearca sa o adauge in lista
    '''
    new_transaction = inputTransaction('Introduceti noua tranzactie:')
    addNewTransaction(new_transaction,data)
    print('Tranzactie adaugata cu succes!\n')


def changeTransactionUI(data):
    '''
        Citste de la tastatura o tranzactie veche si una noua si incearca sa o
        inlocuiasca pe cea veche cu cea noua
    '''
    old_transaction = inputTransaction('Introduceti vechea tranzactie:')
    new_transaction = inputTransaction('Introduceti noua tranzactie:')
    changeTransaction(old_transaction, new_transaction, data)
    print('Modificare efectuata cu succes!\n')


def addTransactionUI(data):
    '''
        Functionalitatea de ADAUGARE
    '''
    print('Type help for instructions\n')

    while True:
        command = input('Meniu ADAUGARE. Introduceti comanda: ')

        if command == 'back':
            print('Inapoi spre meniul principal.\n')
            return
        elif command == 'help':
            print(add_instructions, end='\n\n')
        elif command == 'noua':
            addNewTransactionUI(data)
        elif command == 'modificare':
            changeTransactionUI(data)
        else:
            print('Comanda incorecta!\n')


def deleteTransactionsFromDayUI(data):
    '''
        Citeste o zi si sterge tranzactiile din ziua respectiva
    '''
    day = input('Ziua: ')
    deleteTransactionsFromDay(day,data)
    print('Stergerile au fost efectuate cu succes!\n')


def deleteTransactionsBetweenDaysUI(data):
    '''
        Citeste doua zile si sterge tranzactiile dintre cele doua zile
    '''
    fist_day = input('Prima zi: ')
    last_day = input('Ultima zi: ')
    deleteTransactionsBetweenDays(fist_day, last_day, data)
    print('Stergerile au fost efectuate cu succes!\n')


def deleteTransactionsOfTypeUI(data):
    '''
        Citeste tipul de tranzactie si sterge tranzactiile de tipul respectiv
    '''
    ttype = input('Tip: ')
    deleteTransactionsOfType(ttype, data)
    print('Stergerile au fost efectuate cu succes!\n')


def deleteTransactionsUI(data):
    '''
    Functionalitatea de STERGERE
    '''
    print('Type help for instructions\n')

    while True:
        command = input('Meniu STERGERE. Introduceti comanda: ')

        if command == 'back':
            print('Inapoi spre meniul principal.\n')
            return
        elif command == 'help':
            print(delete_instructions, end='\n\n')
        elif command == 'ziua':
            deleteTransactionsFromDayUI(data)
        elif command == 'perioada':
            deleteTransactionsBetweenDaysUI(data)
        elif command == 'tip':
            deleteTransactionsOfTypeUI(data)
        else:
            print('Comanda incorecta!\n')


def searchTransactionsByAmountUI(data):
    '''
        Citeste o suma si afiseaza tranzacțiile cu sume mai mari decât o suma
    '''
    amount = input('Suma: ')

    trans_list = searchTransactionsByAmount(amount, data)
    printTransactionsUI(trans_list)


def searchTransactionsByAmountAndDateUI(data):
    '''
        Citeste o suma si o zi. Afiseaza tranzactiile cu sume mai mari decat suma
        si care au avut loc inainte de ziua data
    '''
    day = input('Zi: ')
    amount = input('Suma: ')

    trans_list = searchTransactionsByAmountAndDate(amount,day, data)
    printTransactionsUI(trans_list)


def searchTransactionsByTypeUI(data):
    '''
        Citeste un tip de tranzactie si afiseaza tranzactiile de tipul dat
    '''
    ttype = input('Tip: ')

    trans_list = searchTransactionsByType(ttype,data)
    printTransactionsUI(trans_list)


def searchTransactionsUI(data):
    '''
    Functionalitatea de CAUTARE
    '''
    print('Type help for instructions\n')

    while True:
        command = input('Meniu CAUTARE. Introduceti comanda: ')

        if command == 'back':
            print('Inapoi spre meniul principal.\n')
            return
        elif command == 'help':
            print(search_instructions, end='\n\n')
        elif command == 'sume':
            searchTransactionsByAmountUI(data)
        elif command == 'inainte de':
            searchTransactionsByAmountAndDateUI(data)
        elif command == 'tip':
            searchTransactionsByTypeUI(data)
        else:
            print('Comanda incorecta!\n')


def searchAmountOneTypeTransactionsUI(data):
    '''
        Citeste un tip de tranzactie si returneaza suma tranzactiilor de tipul dat
    '''
    ttype = input('Tip: ')

    amount = searchAmountOneTypeTransactions(ttype,data)
    print('Suma tranzactiilor de tipul %d este: %d\n' % (int(ttype), amount))


def searchAmountAtTimeUI(data):
    '''
        Citeste o zi si calculeaza soldul contului la ziua specificata
    '''
    day = input('Zi: ')

    amount = searchAmountAtTime(day,data)
    print('Suma tranzactiilor pana in ziua %d est: %d' % (int(day), amount))


def searchTransactionsByTypeSortedUI(data):
    '''
        Citeste un tip de tranzactii si afiseaza toate tranzactiile de tipul acela, ordonate dupa zi
    '''
    ttype = input('Tip: ')

    trans_list = searchTransactionsByTypeSorted(ttype,data)
    printTransactionsUI(trans_list)


def reportsUI(data):
    '''
        Functionalitatea de RAPORT
    '''
    print('Type help for instructions\n')

    while True:
        command = input('Meniu RAPORT. Introduceti comanda: ')

        if command == 'back':
            print('Inapoi spre meniul principal.\n')
            return
        elif command == 'help':
            print(report_instructions, end='\n\n')
        elif command == 'suma':
            searchAmountOneTypeTransactionsUI(data)
        elif command == 'sold':
            searchAmountAtTimeUI(data)
        elif command == 'ordonat':
            searchTransactionsByTypeSortedUI(data)
        else:
            print('Comanda incorecta!\n')


def filterByTypeAndSumTransactionsUI(data):
    '''
        Citeste un tip de tranzactie si o zi. Elimină toate tranzacțiile mai mici
        decât suma data care au tipul dat
    '''
    ttype = input('Tip: ')
    amount = input('Suma: ')

    filterByTypeAndSumTransactions(ttype,amount,data)
    print('Filtrarea a fost realizata cu succes')


def filterTransactionsUI(data):
    '''
    Functionalitatea de FILTRARE
    '''
    print('Type help for instructions\n')

    while True:
        command = input('Meniu FILTRARE. Introduceti comanda: ')

        if command == 'back':
            print('Inapoi spre meniul principal.\n')
            return
        elif command == 'help':
            print(filter_instructions, end='\n\n')
        elif command == 'tip':
            #filterByTypeTransactionsUI(data)
            deleteTransactionsOfTypeUI(data)
        elif command == 'sumatip':
            filterByTypeAndSumTransactionsUI(data)
        else:
            print('Comanda incorecta!\n')


def undoUI(data):
    undo(data)
