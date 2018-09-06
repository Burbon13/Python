'''
Created on 3 nov. 2017

@author: Rafa
'''
from domain import *
#functia valideaza  cheltuiala
def validareAdaugaCheltuiala(cheltuiala):
    erori=""
    if getZi(cheltuiala)<1 or getZi(cheltuiala)>31:
        erori+="Dati o  zi cuprinsa intre 1 si 31! \n"
    if getTip(cheltuiala)<1 or getTip(cheltuiala)>5:
        erori+="Dati un tip intre 1 si 5! \n"
    if len(erori)>0:
        raise Exception(erori)


def validareIntreg(x):
    try:
        d=int(x)
    except ValueError:
        raise Exception
    else:
        return d
    