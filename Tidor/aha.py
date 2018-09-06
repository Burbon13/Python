dimensiune=int(input("Dati numar:"))
def backRec(x, dim):
    el = -1
    x.append(el)
    while (len(x) <= dim):
        x[-1] = el
        if consistent(x, dim):
            #if solution(x, dim):
            if(len(x) == dim):
                print(x)
            backRec(x, dim)
        el = 1

def consistent(x,dim):
    suma=0
    for i in range(len(x)):
        suma+=x[i]
    if suma<0:
        return False
    return True


def solution(x,dim):
    suma=0
    for i in range(len(x)):
        suma+=x[i]
    return len(x)==dim and suma==0

backRec([],dimensiune)