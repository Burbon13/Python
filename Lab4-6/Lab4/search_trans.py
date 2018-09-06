from utilities import compareDates


def getTransactionsAbove(trans_list, low_amount):
    '''
    Returneaza tranzactiile care au suma mai mare decat o suma data
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    low_amount - numar intreg in functie de care se cauta tranzactiile
    return - lista de tranzactii cautate (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    '''
    above_amount_list = []

    for transaction in trans_list:
        if transaction[1] >= low_amount:
            above_amount_list.append(transaction)

    return above_amount_list


def getTransactionsAboveBefore(trans_list, low_amount, high_date):
    '''
    Returneaza tranzactiile care au suma mai mare decat o suma data
    si care au avut loc inainte de o data specificata
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    low_amount - numar intreg in functie de care se cauta tranzactiile
    high_date - data calendaristica sub forma de touple (zi,luna,an)
    in functie de care se cauta tranzactiile
    return - lista de tranzactii cautate (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    '''
    above_before_list = []

    for transaction in trans_list:
        if transaction[1] >= low_amount and compareDates(high_date,transaction[0]) == 1:
            above_before_list.append(transaction)

    return above_before_list


def getTransactionsOneType(trans_list, type):
    '''
    Returneaza tranzactiile care sunt de un anumit tip
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    type - 0 sau 1, tipul de tranzactii dorite
    return - lista de tranzactii cautate (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    '''
    one_type_list = []

    for transaction in trans_list:
        if transaction[2] == type:
            one_type_list.append(transaction)

    return one_type_list