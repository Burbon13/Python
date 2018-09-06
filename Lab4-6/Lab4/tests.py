from search_trans import getTransactionsAboveBefore
from search_trans import getTransactionsAbove
from search_trans import getTransactionsOneType
from utilities import compareDates
from trans_ex_lists import *


def test_getTransactionsAbove():
    '''
    Testarea functiei getTransactionsAbove()
    '''
    assert getTransactionsAbove(trans_list_ex_1,500) == trans_list_ex_1_limit_500
    assert getTransactionsAbove(trans_list_ex_1, 100) == trans_list_ex_1_limit_100
    assert getTransactionsAbove(trans_list_ex_1, 1000) == trans_list_ex_1_limit_1000
    assert getTransactionsAbove(trans_list_ex_1, 1555) == trans_list_ex_1_limit_1555
    assert getTransactionsAbove(trans_list_ex_1, 2000) == trans_list_ex_1_limit_2000
    assert getTransactionsAbove(trans_list_ex_1, 0) == trans_list_ex_1
    assert getTransactionsAbove(trans_list_ex_1, 200000) == []


def test_getTransactionsAboveBefore():
    '''
    Testarea functiei getTransactionsAboveBefore()
    '''
    assert getTransactionsAboveBefore(trans_list_ex_1,500,date_1) == trans_list_ex_1_limit_500_date_20_6_2016
    assert getTransactionsAboveBefore(trans_list_ex_1,3000,date_1) == trans_list_ex_1_limit_3000_date_20_6_2016
    assert getTransactionsAboveBefore(trans_list_ex_1,1000,date_2) == trans_list_ex_1_limit_1000_date_1_1_2017
    assert getTransactionsAboveBefore(trans_list_ex_1,1,date_3) == trans_list_ex_1_limit_1_date_1_1_1901
    assert getTransactionsAboveBefore(trans_list_ex_1,1,date_4) == trans_list_ex_1


def test_getTransactionsOneType():
    '''
    Testarea functiei getTransactionsOneType
    '''
    assert getTransactionsOneType(trans_list_ex_1,0) == trans_list_ex_1_type_0
    assert getTransactionsOneType(trans_list_ex_1, 1) == trans_list_ex_1_type_1
    assert getTransactionsOneType(trans_list_ex_2, 0) == trans_list_ex_2_type_0
    assert getTransactionsOneType(trans_list_ex_2, 1) == trans_list_ex_2_type_1


def test_compareDates():
    '''
    Verificarea functiei compareDates
    '''
    assert compareDates((13,7,2017),(12,7,2017)) == 1
    assert compareDates((12,12,2012),(12,12,2012)) == 0
    assert compareDates((12,12,2012),(13,12,2012)) == -1
    assert compareDates((3,6,2000),(20,7,2000)) == -1
    assert compareDates((3,8,2000),(12,5,2000)) == 1
    assert compareDates((4,2,2001),(21,12,2000)) == 1
    assert compareDates((13,2,2009),(20,13,2010)) == -1


def run_tests():
    test_getTransactionsAbove()
    test_getTransactionsAboveBefore()
    test_getTransactionsOneType()
    test_compareDates()