from Math import isPrime
from Math import isInRange

def findListWithPrimes(my_list):
    '''
    Functia returneaza secventa de lungime maxima din lista data cu elemente prime
    Input: lista in care se cauta
    Ouput: secventa maximala de numere prime, returnata ca lista
    '''
    max_list = []
    actual_lenght = 0
    for index in range(len(my_list)):
        if isPrime(my_list[index]) == True:
            actual_lenght = actual_lenght + 1
        else:
            if actual_lenght > len(max_list):
                max_list = my_list[index - actual_lenght : index]
            actual_lenght = 0
    if actual_lenght > len(max_list):
        max_list = my_list[len(my_list) - actual_lenght : len(my_list)]
    return max_list


def findListBetweenBounds(my_list, lower_bound, upper_bound):
    '''
    Functia returneaza secventa de lungime maxima din lista data cu elemente cuprinse intre lower_bound si upper_bound
    Input: lista in care se cauta
    Ouput: secventa maximala de numere prime, returnata ca lista
    '''
    max_list = []
    actual_lenght = 0
    for index in range(len(my_list)):
        if  isInRange(my_list[index],lower_bound,upper_bound)== True:
            actual_lenght = actual_lenght + 1
        else:
            if actual_lenght > len(max_list):
                max_list = my_list[index - actual_lenght: index]
            actual_lenght = 0
    if actual_lenght > len(max_list):
        max_list = my_list[len(my_list) - actual_lenght: len(my_list)]
    return max_list


def test_findListWithPrimes():
    assert findListWithPrimes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3]
    assert findListWithPrimes([2, 2, 2, 2]) == [2, 2, 2, 2]
    assert findListWithPrimes([5]) == [5]
    assert findListWithPrimes([4, 4, 4, 4]) == []
    assert findListWithPrimes([8, 2, 3, 5, 7, 3, 4, 3, 2, 4]) == [2, 3, 5, 7, 3]
    assert findListWithPrimes([69, 69, 69]) == []
    assert findListWithPrimes([10, 10, 10, 2]) == [2]
    assert findListWithPrimes([2, 10, 10, 10]) == [2]
    assert findListWithPrimes([2, 2, 10]) == [2, 2]
    assert findListWithPrimes([1, 1, 1, 4, 5, 7, 3]) == [5, 7, 3]


def test_findListBetweenBounds():
    assert findListBetweenBounds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 8) == [4, 5, 6, 7, 8]
    assert findListBetweenBounds([1, 5, 6, 3, 4, 6, 3, ], 1, 5) == [1, 5]
    assert findListBetweenBounds([3, 4, 7, 8], 100, 120) == []
    assert findListBetweenBounds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], -4, 4) == [1, 2, 3, 4]
    assert findListBetweenBounds([1, 2, 3, 4], 1, 4) == [1, 2, 3, 4]
    assert findListBetweenBounds([20, 30, 20, 30, 20], 13, 24) == [20]
    assert findListBetweenBounds([10, 20, 30, 50], 5, 555) == [10, 20, 30, 50]
    assert findListBetweenBounds([1, 2, 3, 7, 8, 9], 4, 6) == []
    assert findListBetweenBounds([1, 2, 3, 4, 5, 7, 3, 5, 8, 10, 20, 10, 3, 4, 5, 6, 3, 5, 6, 3, 4, 11], 3, 14) == [10,3,4,5,6,3,5,6,3,4,11]


def test():
    test_findListWithPrimes()
    test_findListBetweenBounds()


test()