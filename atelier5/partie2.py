import numpy as np
#Question
def my_searchsorted(table:object,indice:int)->int:
    i = 0
    trouve = True
    while  table[i]!= indice   and trouve  :
        if i < len(table) - 1:
            i += 1
        else:
            i = -1
            trouve = False
    return i
arr = np.array([5,9,7,34,71,0,8])
print("L'indice de la valeur rechercher est:",my_searchsorted(arr,34))
print("L'indice de la valeur rechercher est:",my_searchsorted(arr,59))

#Question 2


def my_where(table:object,valeur:int)->list:
    taille_index =len(table)
    res =[]
    for index in range(taille_index):
        if valeur == table[index]:
            res.append(index)
    return res
print("fonction where")
arr2 = np.array([5,9,7,34,9,71,9,0,8])
print("Les indices de la valeur rechercher est:",my_where(arr2,9))

#Question3

def my_add(tableA:object,tableB:object)->object:
    
    if tableA.ndim == tableB.ndim :
        R = np.empty((tableA.ndim,tableA.ndim),dtype=int)
        ligne = tableB.ndim 
        colonne = len(tableB) 
        for index_l in range(ligne):
            for index_col in range(colonne):
                R[index_l,index_col] = tableA[index_l,index_col] + tableB[index_l,index_col]
        return R
    
print("Question 3 fonction")   
A = np.array(([3,1],[6,4]))
B = np.array(([1,8],[4,2]))
print(my_add(A,B))


# Exercice2:

#1) création de matrice
print("exo2.1")
import random as rd
A = np.empty((4,4),dtype=int)

for index_l in range(4):
    for index_col in range(4):
        A[index_l,index_col] = rd.randint(0,10)

print( A )
    
#2) création d'une matrice identité
print("Matrice identité")
I = np.empty((4,4),dtype=int)

for index_l in range(4):
    for index_col in range(4):
        if index_col == index_l:
            I[index_l,index_col] = 1
        else:
            I[index_l,index_col] = 0
print(I)
            
#exercice2.2
def matrice_trace(matrice:object):
    ligne = matrice.ndim
    colonne = len(matrice)
    tr = 0
    for index_l in range(ligne):
        for index_col in range(colonne):
            if index_col == index_l:
                tr += matrice[index_l,index_col]
    return tr
A = np.array(([3,1],[6,4]))
print("fonction matrice_trace")
print(matrice_trace(A))