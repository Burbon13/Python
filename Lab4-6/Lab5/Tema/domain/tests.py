'''
    Modul de TESTARE
'''
import copy
from domain.transactions import *
from domain.test_data import *
from domain.utils import *


def test_addNewTransaction():
    # test0
    data = createDataBase()
    assert getTransactions(data) == []

    #test1
    addNewTransaction(createTransaction(2,200,0),data)
    ans = createDataBase()
    addNewTransaction(createTransaction(2,200,0),ans)
    assert getTransactions(data) == getTransactions(ans)

    #test2
    addNewTransaction(createTransaction(2,200,0),data)
    ans2 = createDataBase()
    addNewTransaction(createTransaction(2,200,0),ans2)
    addNewTransaction(createTransaction(2,200,0),ans2)
    assert getTransactions(data) == getTransactions(ans2)

    #test3
    data = copy.deepcopy(t1)
    addNewTransaction(createTransaction(2,200,0),data)


    #assert getTransactions(data) == getTransactions(t1_1)


def test_changeTransaction():
    #test1
    data = copy.deepcopy(t1)
    try:
        changeTransaction(createTransaction(2,200,0),createTransaction(2,200,1),data)
        assert False
    except ValueError as ve:
        assert str(ve) == 'Tranzactia veche nu a fost gasita in baza de date!\n'

    #test2
    try:
        changeTransaction(createTransaction(2,2200,0),createTransaction(2,200,1),data)
        assert False
    except ValueError as ve:
        assert str(ve) == 'Tranzactia veche nu a fost gasita in baza de date!\n'

    #test3
    data = copy.deepcopy(t2)
    try:
        changeTransaction(createTransaction(3, 1332, 0), createTransaction(2, 200, 1), data)
        assert getTransactions(data) == getTransactions(t2_1)
    except ValueError:
        assert False


def test_deleteTransactionsFromDay():
    #test1
    data = copy.deepcopy(t3)
    deleteTransactionsFromDay('2',data)
    assert getTransactions(data) == getTransactions(t3_1)

    #test2
    deleteTransactionsFromDay('3',data)
    assert getTransactions(data) == getTransactions(t3_2)

    #test3
    deleteTransactionsFromDay('25',data)
    assert getTransactions(data) == getTransactions(t3_3)

    # test3
    deleteTransactionsFromDay('1',data)
    assert getTransactions(data) == getTransactions(createDataBase())


def test_deleteTransactionsBetweenDays():
    #test1
    data = copy.deepcopy(t1)
    deleteTransactionsBetweenDays('1', '14', data)
    assert getTransactions(data) == getTransactions(t1_3)

    #test2
    data = copy.deepcopy(t1)
    deleteTransactionsBetweenDays('2', '25', data)
    assert getTransactions(data) == getTransactions(t1_4)

    #test3
    deleteTransactionsBetweenDays('2','3',data)
    assert getTransactions(data) == getTransactions(t1_4)

def test_deleteTransactionsOfType():
    #test1
    data = copy.deepcopy(t1)
    deleteTransactionsOfType('0',data)
    assert getTransactions(data) == getTransactions(t1_5)

    #test2
    data = copy.deepcopy(t1)
    deleteTransactionsOfType('1',data)
    assert getTransactions(data) == getTransactions(t1_6)



def test_searchTransactionsByAmount():
    #test1
    data = copy.deepcopy(t1)
    assert searchTransactionsByAmount('1000',data) == getTransactions(t1_7)

    #test2
    assert searchTransactionsByAmount('1',data) == getTransactions(t1)

    #test3
    assert searchTransactionsByAmount('111111',data) == getTransactions(createDataBase())

    #test4
    assert searchTransactionsByAmount('2200',data) == getTransactions(t1_8)


def test_searchTransactionsByAmountAndDate():
    #test1
    data = copy.deepcopy(t3)
    assert searchTransactionsByAmountAndDate('150','4',data) == getTransactions(t3_4)

    #test2
    data = copy.deepcopy(t1)
    assert searchTransactionsByAmountAndDate('1000','25',data) == getTransactions(t1_9)

    #test3
    assert searchTransactionsByAmountAndDate('1', '16',data) == getTransactions(t1_10)

    #test4
    data = copy.deepcopy(t2)
    assert searchTransactionsByAmountAndDate('1000','10',data) == getTransactions(t2_2)


def test_searchTransactionsByType():
    #test1
    data = copy.deepcopy(t1)
    assert searchTransactionsByType('1',data) == getTransactions(t1_11)

    #test2
    assert searchTransactionsByType('0',data) == getTransactions(t1_12)


def test_searchAmountOneTypeTransactions():
    #test1
    data = copy.deepcopy(t1)
    assert searchAmountOneTypeTransactions('1',data) == 450

    #test2
    assert searchAmountOneTypeTransactions('0',data) == 3552

    #test3
    data = copy.deepcopy(t2)
    assert searchAmountOneTypeTransactions('1',data) == 12 + 123 + 120

    #test4
    assert searchAmountOneTypeTransactions('0',data) == 33330 + 1532


def test_searchAmountAtTime():
    #test1
    data = copy.deepcopy(t1)
    assert searchAmountAtTime('22',data) == 3540

    #test2
    assert searchAmountAtTime('12',data) == 1220

    #test3
    data = copy.deepcopy(t3)
    assert searchAmountAtTime('3',data) == 35105

    #test4
    assert searchAmountAtTime('30',data) == 35117


def test_searchTransactionsByTypeSorted():
    #test1
    data = copy.deepcopy(t1)
    assert searchTransactionsByTypeSorted('0',data) == getTransactions(ts1)

    #test2
    assert searchTransactionsByTypeSorted('1',data) == getTransactions(ts2)

    # test3
    data = copy.deepcopy(t2)
    assert searchTransactionsByTypeSorted('0',data) == getTransactions(ts3)

    # test4
    assert searchTransactionsByTypeSorted('1',data) == getTransactions(ts4)


def test_filterByTypeAndSumTransactions():
    #test1
    data = copy.deepcopy(t1)
    filterByTypeAndSumTransactions('1','200',data)
    assert getTransactions(data) == getTransactions(ttt1)

    #test2
    filterByTypeAndSumTransactions('0','1500',data)
    assert getTransactions(data) == getTransactions(ttt2)

    #test3
    filterByTypeAndSumTransactions('1','500',data)
    assert getTransactions(data) == getTransactions(ttt3)


def test_undo():
    '''data = createTransactions(list(t1), [], 0)

    addNewTransaction({'day': 22,'amount' : 2200,'ttype' : 0},data)

    undo(data)

    list1 = getTransactions(data)
    list1.sort()
    list2 =  list(t1)
    list2.sort()

    assert list1 == list2'''


def run_tests():
    test_addNewTransaction()
    test_changeTransaction()
    test_deleteTransactionsFromDay()
    test_deleteTransactionsBetweenDays()
    test_deleteTransactionsOfType()
    test_searchTransactionsByAmount()
    test_searchTransactionsByAmountAndDate()
    test_searchTransactionsByType()
    test_searchAmountOneTypeTransactions()
    test_searchAmountAtTime()
    test_searchTransactionsByTypeSorted()
    test_filterByTypeAndSumTransactions()
    test_undo()
    print('<<ALL TESTS ARE GOOD>>')
