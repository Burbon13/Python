from functionalities import addAndModifyTrans
from functionalities import searchTrans
from io_methods import getInt
from io_methods import printTransactions
from ui_texts import Menu_text
from ui_texts import Menu_text_2
from ui_texts import welcome_message
from tests import run_tests


def run1():
    '''
    Functia principala a aplicatiei, afiseaza meniul si asteapta
    ca utilizatorul sa introduca comenzi
    '''
    run_tests()
    transactions_list = []
    functionalities_map = {1 : addAndModifyTrans, 3 : searchTrans}
    print(welcome_message)
    print(Menu_text) #Afiseaza comenzile meniului principal
    while True:
        command = getInt("Introduceti comanda")

        if command == 0:
            print("La revedere")
            break
        elif command in functionalities_map:
            functionalities_map[command](transactions_list)
            print(Menu_text)
        else:
            print("Nu ati introdus o comanda valida")


def run2():
    '''
        Functia principala a aplicatiei, afiseaza meniul si asteapta
        ca utilizatorul sa introduca comenzi
    '''
    run_tests()
    transactions_list = []
    functionalities_map = {"adaugare": addAndModifyTrans, "cautare": searchTrans, "afisare" : printTransactions}
    print(welcome_message)
    print(Menu_text_2)  # Afiseaza comenzile meniului principal
    while True:
        command = input("Introduceti comanda dorita")

        if command == "exit":
            print("La revedere")
            break
        elif command in functionalities_map:
            functionalities_map[command](transactions_list)
            print(Menu_text_2)
        else:
            print("Nu ati introdus o comanda valida")

run1()