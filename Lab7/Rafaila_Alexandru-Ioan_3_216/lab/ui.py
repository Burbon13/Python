'''
Created on 3 nov. 2017

@author: Rafa
'''
from domain import *
from functionalitati import *
from validare import *
from utils import *
def uiUndo(cheltuieli,undolista):
    if len(undolista)==1:
        cheltuieli.pop()
        undolista.pop()
        print(cheltuieli)
        print(undolista)
        
    elif len(undolista)>0:
        undo(cheltuieli,undolista)
   
        print(cheltuieli)
        print(undolista)
    else:
        print("nu se poate realiza undo")

        
def uiCitesteComanda(text):
    a=input(text)
    return a
def uiAdaugaCheltuiala(cheltuieli,undolista):
    ok=1
    a=input("introduceti ziua:")
    b=input("introduceti suma:")
    c=input("introduceti numarul aferent fiecarui tip, 1: mancare, 2:intretinere, 3:imbracaminte, 4 telefon,5:altele")
    try:
        zi=int(a)
    except ValueError:
            ok=0
    try:
        suma=int(b)
    except ValueError:
            ok=0
    try:
        tip=int(c)
    except ValueError:
            ok=0
    if ok==0:
        print("dati valori valide!")
        uiAdaugaCheltuiala(cheltuieli,undolista)
    else:
        try:
            adaugaCheltuiala(cheltuieli, zi, suma, tip)
            adaugareel(undolista)
            copiere(undolista[len(undolista)-1], cheltuieli)
            print(cheltuieli)
            print(undolista)
        except Exception:
            uiAdaugaCheltuiala(cheltuieli,undolista)
def uiActualizareCheltuiala(cheltuieli,undolista):
    poz=zi=sum=tip="a"
    ok=1
    print("alegeti una dintre urmatoarele cheltuieli")
    Afisare(cheltuieli)
    d=input("introduceti nr coresp cheltuielii")
    try:
        poz=int(d)
    except ValueError:
            ok=0
    else:
        if poz<0 or poz>len(cheltuieli):
            ok=0
    
    a=input("introduceti ziua noua :")
    b=input("introduceti suma noua :")
    c=input("introduceti numarul nou aferent fiecarui tip, 1: mancare, 2:intretinere, 3:imbracaminte, 4 telefon,5:altele")
    try:
        zi=int(a)
    except ValueError:
            ok=0
    try:
        suma=int(b)
    except ValueError:
            ok=0
    try:
        tip=int(c)
    except ValueError:
            ok=0
    if ok==0:
        print("dati valori valide!")
        uiActualizareCheltuiala(cheltuieli,undolista)
    else:
        try:
            actualizareCheltuiala(cheltuieli,poz,zi,suma,tip)
            adaugareel(undolista)
            copiere(undolista[len(undolista)-1], cheltuieli)
            print(cheltuieli)
            print(undolista)
        except Exception:
            uiActualizareCheltuiala(cheltuieli,undolista)
def uiCheltuieliMaiMariDecat(cheltuieli,undolista):
    s=input("dati suma:")
    try:
        suma=int(s)
    except ValueError:
        print("dati date corecte!")
        uiCheltuieliMaiMariDecat(cheltuieli,undolista)
    else:
        cheltuieliMaiMariDecatOSuma(cheltuieli, suma)
        
def uiCheltuieliInainteDeZiSiMaiMiciDecatOSuma(cheltuieli,undolista):
    s=input("dati suma:")
    d=input("dati data:")
    data=suma=0
    ok=1
    try:
        suma=validareIntreg(s)
        
    except Exception:
        print("dati valori valide!")
        uiCheltuieliInainteDeZiSiMaiMiciDecatOSuma(cheltuieli,undolista)
    try:
        data=validareIntreg(d)
        if data<1or data>31:
            raise Exception
    except Exception:
        print("dati valori valide!")
        uiCheltuieliInainteDeZiSiMaiMiciDecatOSuma(cheltuieli,undolista)
    cheltuieliInainteDeZiSiMaiMiciDecatOSuma(cheltuieli, data, suma)
def uiCheltuieliDeUnAnumitTip(cheltuieli,undolista):
    var=input("alegeti tipul corespunzator, 1:mancare,2:intretinere, 3:imbracaminte ,4:telefon 5:telefon")   
    try:
        tip=validareIntreg(var)
        if tip<1 or tip>5:
            raise Exception
    except Exception:
        print("dati valori valide!")
        uiCheltuieliDeUnAnumitTip(cheltuieli,undolista)
    else:
        cheltuieliDeUnAnumitTip(cheltuieli, tip)


def uiStergeMultiplii(cheltuieli,undolista):
    stergereMultiplii(cheltuieli)
    adaugareel(undolista)
    copiere(undolista[len(undolista) - 1], cheltuieli)
    print(cheltuieli)
    print(undolista)


def uiStergeCheltuieliDinZi(cheltuieli,undolista):
    var=input("dari ziua:")
    try:
        zi=validareIntreg(var)       
        if zi<1 or zi >31:
            raise Exception
    except Exception: 
        print("dati valori valide!")
        uiStergeCheltuieliDinZi(cheltuieli,undolista)
    stergereCheltuieliDinZi(cheltuieli, zi)
    adaugareel(undolista)
    copiere(undolista[len(undolista)-1], cheltuieli)
    print(cheltuieli)
    print(undolista)
def uiStergeCheltuieliInterval(cheltuieli,undolista):
    var1=input("dati un capat al intervalului:")
    var2=input("dati celalalt capat al intervalului:")
    inc=sf=33
    try:
        inc=validareIntreg(var1) 
        
            
    except Exception: 
        print("dati valori valide!")
        uiStergeCheltuieliInterval(cheltuieli,undolista)
    else:
        if inc<1 or inc >31:
            print("dati valori valide!")
            uiStergeCheltuieliInterval(cheltuieli,undolista)
        else:
            try:
                sf=validareIntreg(var2)       
        
            except Exception: 
                print("dati valori valide!")
                uiStergeCheltuieliInterval(cheltuieli,undolista)
            else:
                if sf<1 or sf >31:
                    print("dati valori valide!")
                    uiStergeCheltuieliInterval(cheltuieli,undolista)
                else:
                    if inc<sf:
                        stergeCheltuieliInterval(cheltuieli, inc, sf)
                        adaugareel(undolista)
                        copiere(undolista[len(undolista)-1], cheltuieli)
                        print(cheltuieli)
                        print(undolista)
                    else:
                        stergeCheltuieliInterval(cheltuieli, sf,inc)
                        adaugareel(undolista)
                        copiere(undolista[len(undolista)-1], cheltuieli)
                        print(cheltuieli)
                        print(undolista)
def uiStergeCheltuieliTip(cheltuieli,undolista):
    var=input("alegeti tipul corespunzator, 1:mancare,2:intretinere, 3:imbracaminte ,4:telefon 5:telefon")      
    try:
        tip=validareIntreg(var)
    except Exception:
        print("dati date valide:")     
        uiStergeCheltuieliTip(cheltuieli,undolista)  
    else:
        stergeCheltuieliDeTip(cheltuieli,tip)
        adaugareel(undolista)
        copiere(undolista[len(undolista)-1], cheltuieli)
        print(cheltuieli)
        print(undolista) 
        
   
def uiSumaTotalTip(cheltuieli,undolista):    
    var=input("alegeti tipul corespunzator, 1:mancare,2:intretinere, 3:imbracaminte ,4:telefon 5:telefon")
    try:
        tip=validareIntreg(var)
    except Exception:
        print("dati date valide:")     
        uiSumaTotalTip(cheltuieli,undolista)  
    else:
        print(sumaTotalaTip(cheltuieli,tip))
def uiCheltuieliCuAnumitaSuma(cheltuieli,undolista):
    var=input("dati suma:")
    try:
        suma=validareIntreg(var)
        
    except Exception:
        print("dati date valide:")
        uiCheltuieliCuAnumitaSuma(cheltuieli,undolista)
    else:
        cheltuieliCuAnumitaSuma(cheltuieli, suma)
def uiZiuaCuSumaMax(cheltuieli,undolista):  
    print(ziuaCuSumaMax(cheltuieli))   
def uiSortareTip(cheltuieli,undolista):      
    sortareTip(cheltuieli)
    adaugareel(undolista)
    copiere(undolista[len(undolista)-1], cheltuieli)
    print(cheltuieli)
    print(undolista) 
def uiElChelMaiMiciCaSuma(cheltuieli,undolista):
    var=input("dati suma")
    try:
        suma=validareIntreg(var)
    except Exception:
        print("dati date valide:") 
        uiElChelMaiMiciCaSuma(cheltuieli,undolista)
    else:
        elChelMaiMiciCaSuma(cheltuieli,suma)
        adaugareel(undolista)
        copiere(undolista[len(undolista)-1], cheltuieli)
        print(cheltuieli)
        print(undolista)
    