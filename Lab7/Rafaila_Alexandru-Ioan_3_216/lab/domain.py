'''
Created on 3 nov. 2017

@author: Rafa
'''
from utils import *
def adaugareel(lista):
    l=[]
    lista.append(l)
def copiereundo(cheltuieli,undolista):
    '''if len(undolista[len(undolista)-1])> len(cheltuieli):
        a=len(cheltuieli)
    else:
        a=len(undolista[len(undolista)-1])
                        
    for i in range(0,a):
        chcheltuieli[i]=undolista[len(undolista)-1][i]eltuieli[i]=undolista[len(undolista)-1][i]
    for i in range(0,len(cheltuieli)-a):
        cheltuieli.pop()
    '''   
    for i in range(len(undolista[len(undolista)-1]),len(cheltuieli)):
        cheltuieli.pop()
    for i in range(0,len(undolista[len(undolista)-1])):
        if i<len(cheltuieli):
            cheltuieli[i]=undolista[len(undolista)-1][i]
        else:
            cheltuieli.append({})
            cheltuieli[i]=undolista[len(undolista)-1][i]
        
def creaeazaCheltuiala(zi,suma,tip):
    return {"zi":zi,"suma":suma,"tip":tip}
def getZi(cheltuiala):
    return cheltuiala["zi"]
def getSuma(cheltuiala):
    return cheltuiala["suma"]
def getTip(cheltuiala):
    return cheltuiala["tip"]

def setZi(cheltuiala,zi):
    cheltuiala["zi"]=zi
def setSuma(cheltuiala,suma):
    cheltuiala["suma"]=suma
def setTip(cheltuiala,tip):
    cheltuiala["tip"]=tip
def cheltuialaMaiMicaDecatOSuma(cheltuiala,s):
    if cheltuiala["suma"]<s:
        return True
    else:
        return False
def cheltuialaInainteDeOData(cheltuiala,data):
    if cheltuiala["data"]<data:
        return True
    else:
        return False


