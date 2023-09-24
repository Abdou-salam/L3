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