'''
    Modulul tranzactii, contineu functii legate de tranzactii
'''
from ui.validation import validateTransaction
from ui.validation import validateDay
from ui.validation import validateType
from ui.validation import validateAmount
from domain.utils import *


def addNewTransaction(new_transaction, data):
    '''
        Adauga o noua tranzactie in lista
        new_transaction - tranzactia de adaugat
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    validateTransaction(new_transaction)

    addTransaction(data, new_transaction)


def changeTransaction(old_transaction, new_transaction, data):
    '''
        Schimba o tranzactie veche cu una noua
        old_transaction - tranzactia de inlocuit
        new_transaction - tranzactia inlocuitoare
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    validateTransaction(old_transaction)
    validateTransaction(new_transaction)

    if transExists(data, old_transaction) == False:
        raise ValueError('Tranzactia veche nu a fost gasita in baza de date!\n')

    swapTransaction(data,old_transaction,new_transaction)


def deleteTransactionsFromDay(day, data):
    '''
        Sterge tranzactiile de la o zi specificata
        day (string) - ziua din care se sterg tranzactiile
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateDay(day)
    day = int(day)

    to_delete_list = []

    for trans in transactions:
        if getDay(trans) == day:
            to_delete_list.append(trans)

    deleteTransactions(data, to_delete_list)


def deleteTransactionsBetweenDays(first_day, last_day, data):
    '''
        Sterge tranzactiile dintre doua zile specificate
        fist_day, last_day (string) - zilele dintre care se sterg tranzactiile
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateDay(first_day)
    validateDay(last_day)
    first_day = int(first_day)
    last_day = int(last_day)

    to_delete_list = []

    for trans in transactions:
        if first_day <= getDay(trans) <= last_day:
            to_delete_list.append(trans)

    deleteTransactions(data, to_delete_list)


def deleteTransactionsOfType(ttype, data):
    '''
        Sterge tranzactiile de un anume tip specificat
        ttype (string) - tipul tranzactiilor de sters
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateType(ttype)
    ttype = int(ttype)

    to_delete_list = []

    for trans in transactions:
        if getType(trans) == ttype:
            to_delete_list.append(trans)

    deleteTransactions(data, to_delete_list)


def searchTransactionsByAmount(amount, data):
    '''
        Returneaza o lista cu tranzactiile care au suma mai mare decat o suma data
        amount (string) - suma in functie de care se cauta
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateAmount(amount)
    amount = int(amount)

    trans_list = []

    for trans in transactions:
        if getAmount(trans) >= amount:
            trans_list.append(trans)

    return trans_list


def searchTransactionsByAmountAndDate(amount,day,data):
    '''
        Returneaza o lista cu tranzactiile care au suma mai mare decat o suma data
        si care au avut loc inainte de o zi data
        amount (string) - suma in functie de care se cauta
        day (string) - ziua in functie de care se cauta
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateAmount(amount)
    validateAmount(day)
    amount = int(amount)
    day = int(day)

    trans_list = []

    for trans in transactions:
        if getAmount(trans) >= amount and getDay(trans) <= day:
            trans_list.append(trans)

    return trans_list


def searchTransactionsByType(ttype, data):
    '''
        Returneaza o lista cu tranzactiile de un anumit tip
        ttype (string) - tipul de tranzactie in functie de care se cauta
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateType(ttype)
    ttype = int(ttype)

    trans_list = []

    for trans in transactions:
        if getType(trans) == ttype:
            trans_list.append(trans)

    return trans_list


def searchAmountOneTypeTransactions(ttype, data):
    '''
        Returneaza suma tranzactiilor de un anumit tip
        ttype (string) - tipul de tranzactie in functie de care se cauta
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateType(ttype)
    ttype = int(ttype)

    sum = 0

    for trans in transactions:
        if getType(trans) == ttype:
            sum += getAmount(trans)

    return sum


def searchAmountAtTime(day, data):
    '''
        Returneaza soldul contului la o anumita zi
        day (string) - ziua in functie de care se cauta
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateDay(day)
    day = int(day)

    sum = 0

    for trans in transactions:
        if getDay(trans) <= day:
            sum += getAmount(trans)

    return sum


from operator import itemgetter

def searchTransactionsByTypeSorted(ttype, data):
    '''
        Returneaza tranzactiile de un anumit tip, ordonate dupa zile
        ttype (string) - tipul in functie de care se cauta tranzactiile
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    trans_list = searchTransactionsByType(ttype, data)

    trans_list = sorted(trans_list)

    return trans_list


def filterByTypeAndSumTransactions(ttype, amount, data):
    '''
        Sterge tranzactiile de un anumit tip si care au suma mai mica decat una daa
        ttype (string) - tipul in functie de care se sterge
        amount (string) - ziua in functie de care se sterge
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)

    validateType(ttype)
    validateAmount(amount)
    ttype = int(ttype)
    amount = int(amount)

    to_delete_list = []

    for trans in transactions:
        if getType(trans) == ttype and getAmount(trans) <= amount:
            to_delete_list.append(trans)

    deleteTransactions(data, to_delete_list)


def undo(data):
    '''
        Reface lista de tranzactii sa fie identica cu cea care era inainte
        de efectuarea ultimei operatii
        data - dictionar care contine tranzactiile, istoricul si nr de operatii efectuate
             - {'transactions':[],'undo_list':[],'operations':int}
    '''
    transactions = getTransactions(data)
    undo_list = getUndo(data)
    pos = len(undo_list) - 1


    while pos >= 0 and getUndoNr(undo_list[pos]) == getOperations(data):

        #trans = undo_list[pos][2]
        trans = getUndoTransaction(undo_list[pos])

        if getUndoType(undo_list[pos]) == 0:
            transactions.remove(trans)
        else:
            transactions.append(trans)

        undo_list.pop()

        pos = pos - 1

    if getOperations(data) > 0:
        setOperations(data, getOperations(data) - 1)
        print('Undo efectuat cu succes')
    else:
        print('Nu mai este ce undo sa se faca!\n')