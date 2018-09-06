def isPrime(number):
    if number <= 1 or number % 2 == 0 and number != 2:
        return False
    d = 3

    while d * d <= number:
        if number % d == 0:
            return False
        d = d + 2

    return True


def test_isPrime():
    assert isPrime(-4) == False
    assert isPrime(0) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(9) == False
    assert isPrime(12) == False


test_isPrime()