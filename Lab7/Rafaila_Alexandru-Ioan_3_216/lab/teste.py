'''
Created on 10 nov. 2017

@author: Rafa
'''
from ui import *
from functionalitati import *
def test_uiUndo():
    l=[{'zi':1, 'suma':1, 'tip':1},{'zi':2, 'suma':2, 'tip':2}]
    undolist=[[{'zi':1, 'suma':1, 'tip':1}],[{'zi':1, 'suma':1, 'tip':1},{'zi':2, 'suma':2, 'tip':2}]]
    uiUndo(l, undolist)
    assert len(l)==1
    uiUndo(l, undolist)
    assert len(l)==0
   
def test_adaugaCheltuiala():
    l=[]
    adaugaCheltuiala(l,1,1,1)
    assert len(l)==1
    adaugaCheltuiala(l,2,2,2)
    assert len(l)==2
def test_actualizareCheltuiala():
    l=[{'zi':1, 'suma':1, 'tip':1}]
    actualizareCheltuiala(l,0,2,2,2)
    assert l[0]=={'zi':2, 'suma':2, 'tip':2}
def test_stergeCheltuieliDinZI():
    l=[{'zi':1, 'suma':1, 'tip':1},{'zi':2, 'suma':2, 'tip':2}]
    stergereCheltuieliDinZi(l,2)
    assert len(l)==1
def test_stergeCheltuieliInterval():
    l=[{'zi':1, 'suma':1, 'tip':1},{'zi':2, 'suma':2, 'tip':2}]
    stergeCheltuieliInterval(l, 2,4) 
    assert len(l)==1
def test_elCheltuieliMaiMiciDecat():
    l=[{'zi':1, 'suma':1, 'tip':1},{'zi':2, 'suma':3, 'tip':2}]
    elChelMaiMiciCaSuma(l,2)
    assert len(l)==1        
def teste():
    test_actualizareCheltuiala()
    test_adaugaCheltuiala()
    test_elCheltuieliMaiMiciDecat()
    test_stergeCheltuieliDinZI()
    test_stergeCheltuieliInterval()
    test_uiUndo()
