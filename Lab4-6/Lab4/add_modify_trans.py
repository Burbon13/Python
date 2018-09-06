def addNewTransaction(trans_list, transaction):
    '''
    Adauga o tranzactie in lista de tranzactii.
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an)).
    transaction - tranzactie (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an)).
    '''
    trans_list.append(transaction)


def modifyTransaction(trans_list, old_transaction, new_transaction):
    '''
    Modifica o tranzactie. In cazul in care aceasta nu exista, se afiseaza
    un mesaj corespunzator.
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an)).
    old_transaction - tranzactie veche(o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an)).
    new_transaction - tranzactia noua care o va inlocui pe cea veche
    (o tranzactie este un touple de forma (data,suma,tip) iar data este
    un touple de forma (zi,luna,an)).
    '''
    if old_transaction in trans_list:
        trans_list.remove(old_transaction)
        trans_list.append(new_transaction)
    else:
        print("Tranzactia pe care doriti sa o schimbati nu exista!")