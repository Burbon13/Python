'''
Created on 3 nov. 2017

@author: Rafa
'''
from domain import *
from functionalitati import *
from validare import *
from utils import *
from meniu import *
from ui import *
from teste import *
def run():
    cheltuieli=[]
    undolista=[]
    teste()
    comenzi={"el":uiElChelMaiMiciCaSuma,"add":uiAdaugaCheltuiala,"act":uiActualizareCheltuiala,
             "cauta1":uiCheltuieliMaiMariDecat,"cauta2":uiCheltuieliInainteDeZiSiMaiMiciDecatOSuma,
             "cauta3":uiCheltuieliDeUnAnumitTip,"sterge1":uiStergeCheltuieliDinZi,
             "sterge2":uiStergeCheltuieliInterval,"sterge3":uiStergeCheltuieliTip,
             "rap1":uiSumaTotalTip,"rap2":uiZiuaCuSumaMax,"rap3":uiCheltuieliCuAnumitaSuma,
             "rap4":uiSortareTip,"undo":uiUndo,"TARE":uiStergeMultiplii}
    while True:
        meniu()
        cmd= uiCitesteComanda("dati comanda")
        if cmd=="exit":
            break
        else:
            if cmd in comenzi:
                comenzi[cmd](cheltuieli,undolista)
            else:
                print("comanda invalida!")
run()