n = int(input()) - 1

truth = True

number = 2

while truth == True:
    d = 2
    aux = number
    while aux > 1 and truth == True:
        if aux % d == 0:
            n = n - 1
            if n == 0:
                print(d)
                truth = False
            while aux % d == 0:
                aux //= d
        d = d + 1
    number = number + 1



