def isPrime(number):
    '''
    Verifica daca un numar este prim
    input - numarul de verificat
    output - True daca este prim
             False altfel
    '''
    if number < 2 or number % 2 == 0 and number != 2:
        return False
    val = 3
    while val * val <= number:
        if number % val == 0:
            return False
        val = val + 2
    return True

def isInRange(value, lower_bound, upper_bound):
    '''
    Verifica daca o valoare apartine intr-un interval
    Input: valoarea si marginile intervalului
    Returneaza True daca apartine
    Returneaza False altfel
    '''
    return value >= lower_bound and value <= upper_bound

def test_isPrime():
    assert isPrime(-100) == False
    assert isPrime(-10) == False
    assert isPrime(-1) == False
    assert isPrime(0) == False
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(9) == False
    assert isPrime(63) == False
    assert isPrime(997) == True
    assert isPrime(1002) ==  False
    assert isPrime(5) ==  True

test_isPrime()