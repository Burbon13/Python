from domain.numbers import isPrime

def isPrimeUI(number):
    primalitate = isPrime(number)

    print("Numarul %d este: " % (number), end="")

    if primalitate == True:
        print("prim.")
    else:
        print("neprim.")
