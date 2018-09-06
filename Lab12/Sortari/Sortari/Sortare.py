'''
Created on 18 dec. 2017

@author: Stefan
'''
def sortareInterClasare(lista,key=lambda x:x,cmp=lambda x,y:x<y,reverse=False):
    if len(lista)==1:
        return lista
    primele=sortareInterClasare(lista[:len(lista)//2], key, cmp, False)
    ultimele=sortareInterClasare(lista[len(lista)//2:], key, cmp, False)    
    rez=[]
    pozp=0
    pozu=0
    while pozp<len(primele) and pozu<len(ultimele):
        if cmp(key(primele[pozp]),key(ultimele[pozu])):
            rez.append(primele[pozp])
            pozp+=1
        else:
            rez.append(ultimele[pozu])
            pozu+=1
    if pozp<len(primele):
        rez+=primele[pozp:]
    if pozu<len(ultimele):
        rez+=ultimele[pozu:]
    if reverse==True:
        rez.reverse()   
    return rez



def maxim(a,b,key=lambda x:x, cmp=lambda x,y:x<y):
    if cmp(key(a), key(b)):
        return a
    return b

def heapifyDown(lista, start, stop,key=lambda x:x, cmp=lambda x,y:x<y, reverse=False):
    print("hupDown")
    print(lista)
    print(start,stop)
    current = start
    maximl = maxim(lista[current*2+1], lista[current*2+2])
    ok = True
    while ok and current < stop//2:
        ok = False
        if maximl == lista[current*2+1] and cmp(key(maximl), key(lista[current])):
            aux = lista[current]
            lista[current] = lista[current*2+1]
            lista[current*2+1] = aux
            current = current*2+1
            ok = True
            continue
        if current*2+2 < len(lista) and maximl == lista[current*2+2] and cmp(key(maximl), key(lista[current])):
            aux = lista[current]
            lista[current] = lista[current*2+2]
            lista[current*2+2] = aux
            current = current*2+2
            ok = True
            continue
        

def heapifyUp(lista, start, stop,key=lambda x:x, cmp=lambda x,y:x<y, reverse=False):
    current = stop
    ok = True
    while ok and current > 0:
        ok = False
        parinte = (current-1)//2
        print(parinte, current)
        if maxim(lista[parinte], lista[current]) == lista[parinte]:
            print(lista)
            print("swap")
            aux = lista[parinte]
            lista[parinte] = lista[current]
            lista[current] = aux
            current = parinte
            ok = True
        
    
def sortareHeap(lista, stanga, mijloc, dreapta, flag=True, key=lambda x:x, cmp=lambda x,y:x<y, reverse=False):
    print(lista)
    if flag == True and mijloc >= dreapta:
        print("flag")
        aux = lista[stanga]
        lista[stanga] = lista[dreapta]
        lista[dreapta] = aux
        heapifyDown(lista, stanga, mijloc-1, key=lambda x:x, cmp=lambda x,y:x<y, reverse=False)
        return sortareHeap(lista, stanga, mijloc-1, dreapta, False, key, cmp, reverse)
    if flag == False and stanga == mijloc:
        if reverse == True:
            lista.reverse()
        return lista
    if flag == False:
        aux = lista[stanga]
        lista[stanga] = lista[dreapta]
        lista[dreapta] = aux
        heapifyDown(lista, stanga, mijloc, key=lambda x:x, cmp=lambda x,y:x<y, reverse=False)
        return sortareHeap(lista, stanga, mijloc-1, dreapta, False, key, cmp, reverse)
    mijloc = mijloc+1
    print("hup")
    heapifyUp(lista, stanga, mijloc, key=lambda x:x, cmp=lambda x,y:x<y, reverse=False)
    return sortareHeap(lista, stanga, mijloc, dreapta, True, key, cmp, reverse)

def sorteaza(lista,key=lambda x:x,cmp=lambda x,y:x<y,reverse=False):
    #return sortareInterClasare(lista, key, cmp, reverse)
    return sortareHeap(lista, 0, 0, len(lista)-1, True, key, cmp, reverse)

sortat=sorteaza([1,3,2,4,7,12,-1,8,6],reverse=True,key=lambda x:-x,cmp=lambda x,y:x>y)
print(sortat)