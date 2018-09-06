x = int(input())

def e_prim(numar):
    if numar < 2 or numar % 2 == 0 and numar != 2:
        return False
    d = 3
    while d * d <= numar:
        if numar % d == 0:
            return False
        d = d + 2
    return True

while True:
    x = x + 1
    if e_prim(x) == True:
        print("Numarul prim gasit : ", x)
        break

