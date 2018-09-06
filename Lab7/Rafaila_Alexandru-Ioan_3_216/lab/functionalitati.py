'''
Created on 3 nov. 2017

@author: Rafa
'''
from domain import *
from validare import *
from utils import *
def undo(cheltuieli,undolista):
    undolista.pop()
    #if len(undolista)>0:
    copiereundo(cheltuieli,undolista)
    
    
def elChelMaiMiciCaSuma(cheltuieli,suma):
    d=0
    n=len(cheltuieli)
    for i in range(0,n):
        if  cheltuieli[i-d]["suma"]<suma:
            del cheltuieli[i-d]
            d+=1
        
       
def adaugaCheltuiala(cheltuieli,zi,suma,tip):
    cheltuiala=creaeazaCheltuiala(zi,suma,tip)
    try:
        validareAdaugaCheltuiala(cheltuiala)
    except Exception:
        print("dati date valide!")
        raise Exception
    
      
    else:
        cheltuieli.append(cheltuiala)
def actualizareCheltuiala(cheltuieli,poz,zi,suma,tip):
    cheltuiala=creaeazaCheltuiala(zi,suma,tip)
    try:
        validareAdaugaCheltuiala(cheltuiala)
    except Exception:
        print("dati date valide!")
        raise Exception
    else:
        cheltuieli[poz]=cheltuiala
def cheltuieliMaiMariDecatOSuma(cheltuieli,suma):
    for i in cheltuieli:
        if i["suma"]>suma:
            print(i)
def cheltuieliInainteDeZiSiMaiMiciDecatOSuma(cheltuieli,data,suma):
    for i in cheltuieli:
        if cheltuialaInainteDeOData(i, data)==True and cheltuialaMaiMicaDecatOSuma(i, suma):
            print(i)
def cheltuieliDeUnAnumitTip(cheltuieli,tip):
    for i in cheltuieli:
        if i["tip"]==tip :
            print(i)


def stergereMultiplii(cheltuieli):
    d = 0
    n = len(cheltuieli)
    for i in range(0, n):
        if cheltuieli[i - d]["suma"] % 10 == 0:
            del cheltuieli[i - d]
            d += 1


def stergereCheltuieliDinZi(cheltuieli,zi):
    d=0
    n=len(cheltuieli)
    for i in range(0,n):
        if  cheltuieli[i-d]["zi"]==zi:
            del cheltuieli[i-d]
            d+=1
def stergeCheltuieliInterval(cheltuieli,inc,sf):
    for i in range(inc,sf+1):
        stergereCheltuieliDinZi(cheltuieli,i)
def stergeCheltuieliDeTip(cheltuieli,tip):
    d=0
    n=len(cheltuieli)
    for i in range(0,n):
        if  cheltuieli[i-d]["tip"]==tip:
            del cheltuieli[i-d]
            d+=1
def sumaTotalaTip(cheltuieli,tip):
    s=0
    for i in cheltuieli:
        if i["tip"]==tip:
            s=s+i["suma"]
    return s
def cheltuieliCuAnumitaSuma(cheltuieli,suma):
    for i in cheltuieli:
        if i["suma"]==suma:
            print(i)
def ziuaCuSumaMax(cheltuieli):
    zile=[0]*31
    max=0
    j=0
    for i in cheltuieli:
        zile[i[0]]+=i["suma"]  
    for i in zile:
        if i>max:
            max=i
            zi=j
        j+=1
            
    return zi
def sortareTip(cheltuieli):
    n=len(cheltuieli)
    for i in range(0,n):
        for j in range(i+1,n):
            if cheltuieli[i]["tip"]>cheltuieli[j]["tip"]:
                a=cheltuieli[i]["tip"]
                cheltuieli[i]["tip"]=cheltuieli[j]["tip"]
                cheltuieli[j]["tip"]=a