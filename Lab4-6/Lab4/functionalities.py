from io_methods import getInt
from io_methods import getTransaction
from io_methods import printTransactions
from io_methods import getDate
from ui_texts import addAndModifyTrans_text
from ui_texts import searchTrans_text
from add_modify_trans import *
from search_trans import *

def addAndModifyTrans(trans_list):
    '''
    Functionalitatea de "Adaugare" in care utilizatorul
    alege comanda pe care doreste sa o execute.
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    return - nimic
    '''
    print(addAndModifyTrans_text) #Afiseaza operatiile posibile

    command = input("Introduceti comanda")

    if command == "back":
        print("Intoarcere la meniul principal\n")
        return
    elif command == "noua":
        transaction = getTransaction("Introduceti tranzactia")
        addNewTransaction(trans_list, transaction)
    elif command == "modifica":
        old_transaction = getTransaction("Introduceti vechea tranzactie")
        new_transaction = getTransaction("Introduceti noua tranzactie")
        modifyTransaction(trans_list, old_transaction, new_transaction)
    else:
        print("Nu ati introdus o comanda valida")


def searchTrans(trans_list):
    '''
    Functionalitatea de "Cautari" in care utilizatorul
    alege comanda pe care doreste sa o execute.
    trans_list - lista de tranzactii (o tranzactie este un touple de
    forma (data,suma,tip) iar data este un touple de forma (zi,luna,an))
    return - nimic
    '''
    print(searchTrans_text) #Afiseaza operatiile posibile

    command = input("Introduceti comanda")

    if command == "back":
        print("Intoarcere la meniul principal\n")
    elif command == "sume":
        low_amount = getInt("Tipareste tranzactiile cu sume mai mari decat:")
        printTransactions(getTransactionsAbove(trans_list,low_amount))
    elif command == "inainte de":
        low_amount = getInt("Tipareste tranzactiile cu sume mai mari decat:")
        high_date = getDate("Tipareste tranzactiile inainte de data de:")
        printTransactions(getTransactionsAboveBefore(trans_list,low_amount,high_date))
    elif command == "tip":
        transaction_type = getInt("Introduceti tipul de tranzactie (0 - Adaugare/1 - Retragere)")
        printTransactions(getTransactionsOneType(trans_list,transaction_type))
    else:
        print("Nu ati introdus o camanda valida")