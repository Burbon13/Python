'''
Created on 3 nov. 2017

@author: Rafa
'''

def Afisare(cheltuieli):
    j=0
    for i in cheltuieli:
       print(j,i)
       j+=1 
def copiere1(l1,l2):
    for i in range(0,len(l1)):
        l1[i]=l2[i]
def copiere(l1,l2):
    for i in l2:
        l1.append(0)
    for i in range(0,len(l1)):
        l1[i]=l2[i]