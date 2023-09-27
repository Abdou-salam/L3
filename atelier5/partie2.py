import numpy as np
#Question
def my_searchsorted(table:object,indice:int)->int:
    i = 0
    
    while  table[i]!= indice   and i != -1  :
        if i < len(table) - 1:
            i += 1
        else:
            i = -1
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


print("  ")
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

print("fonction est symetrie")
def est_symetrique(matrice:object)->bool:
    ligne = matrice.shape[0]
    colonne = matrice.shape[1]
    res = False
    for index_l in range(ligne):
        for index_col in range(colonne):
            if matrice[index_l,index_col] != matrice[index_col,index_l]:
                res = False
                break
            else:
                res = True
    return res

A = np.array(([3,1],[6,4]))
B = np.array(([1,8],[8,1]))
print("Matrice:",A,"\t",est_symetrique(A))
print("Matrice:",B,"\t",est_symetrique(B))

#Methode 2
#def est_symetrique2(matrice:object)->bool:
 #   ligne = matrice.ndim - 1
  #  colonne = len(matrice) - 1
   # index_col = 0
    #index_l  = 0
    #res =True
    #while index_l != ligne and res:
     #   while index_col != colonne and res  :
      #      if matrice[index_l,index_col] == matrice[index_col,index_l]:  
              #    index_col += 1
              #    res =True
         #     else:
           #       res = False
                
      #    index_l  += 1        
   #   return res
#  c = np.array(([5,0],[8,4]))
#  d = np.array(([2,9],[9,2]))
#  print("meyhode2 fonction est_semetrique")
#  print("Matrice:",c,"\t",est_symetrique2(c))
#  print("Matrice:",d,"\t",est_symetrique2(d))


def produit_diagonal(matrice:object)->int:
    ligne = matrice.shape[0]
    colonne = matrice.shape[1]
    produit = 1
    for index_l in range(ligne):
        for index_col in range(colonne):
            if index_l == index_col:
                produit *= matrice[index_l,index_col]
    return produit
print("produit diagonal")
A = np.array(([3,1],[6,4]))
print(produit_diagonal(A))

#3)Application des fonctions

print("application des fonction\n")
A = np.array([[1,2],[3,4]])
print("trace de",A, "est:",matrice_trace(A))
print("calcule du produit des élément de la diagonale")
print("le produit de:",A,"est:",produit_diagonal(A))
print("symetrie de :",A)
mat = (A + A.T)/2
print(est_symetrique(mat))
print("\n")
#4) Manipulation supplémentaire

#partie 3

def matriceAdjacences(S:list,A:list)->object:
    ligne = len(S)
    colonne = len(S)
    taille_index = len(A)
    
    mat = np.zeros([ligne,colonne])

    for index in range(taille_index):
        tmp = A[index]
        mat[tmp[0],tmp[1]]= 1

    for index_l in range(ligne):
        for index_col in range(colonne):
            if  mat[index_l,index_col] != 1:
                mat[index_l,index_col] = 0
    return mat
sommet = [0,1,2,3,4]
arc =[(0,1),(0,2),(1,2),(1,4),(2,3),(3,4),(4,2)]

print("matriceAdjacence")
print(matriceAdjacences(sommet,arc))
print("\n")

#matriceAdjacencePond

def matriceAdjacencePond(S,A):
    ligne = len(S)
    colonne = len(S)
    taille_index = len(A)
    
    mat = np.zeros([ligne,colonne])

    for index in range(taille_index):
        tmp = A[index]
        mat[tmp[0],tmp[1]]= tmp[2]

    for index_l in range(ligne):
        for index_col in range(colonne):
            if  mat[index_l,index_col] == "":
                mat[index_l,index_col] = 0
    return mat
sommet2 = [0,1,2,3,4]
print("atriceAdjacencePond")
arc2= [[0,1,40], [0,2,21], [1,4,44], [1,2,14],[2,3,10], [3,4,35], [4,2,23]]
print(matriceAdjacencePond(sommet2,arc2))
print("\n")

# 3)lireMatriceFichier
#def lireMatriceFichier(nomfichier):
   # f = open(nomfichier,"r")
   # c = f.readline()
    #lst =[]
   # compteur = 0
    #ligne = len(c)
    #while c != "" :
    #    compteur += 1
    #    c = f.readline()
     

   # mat = np.array([ligne,compteur])

   # index_l = 0
   # index_col = 0
   # while c != "" :
        #for val in c.split():
           # mat[index_l,index_col] = val
          #  index_l += 1
           
       # c = f.readline()
       # index_col += 1
   # return mat

    
    
#fic = 'C:/Users/Etudiant/Desktop/L3/atelier5/graph1.txt'

#print(lireMatriceFichier(fic))



#4) tousLesSommets

def tousLesSommets(mat):

    ligne = mat.shape[0]
    colonne = mat.shape[1]
    lst =[]
    if ligne == colonne:
        for index in range(ligne):
            lst.append(index)
        return lst
print("tousLesSommets")
mat = np.array([[1,0,1,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]])
print(tousLesSommets(mat))
print("\n")

#5)listeArcs(mat)

def  listeArcs(mat):
    ligne = mat.shape[0]
    colonne = mat.shape[1]
    lst = []
    for index_l in range(ligne):
        for index_col in range(colonne):
            if mat[index_l,index_col] == 1:
                lst.append((index_l,index_col))
    return lst
mat1 = np.array([[1,0,1,0],[1,1,0,0],[1,0,0,0],[0,0,0,0]])
print("listeArcs")
print("la matrice est:",mat)
print(listeArcs(mat))

#6) matriceIncidence

def matriceIncidencer(mat):
    ligne = mat.shape[0]
    colonne = len(listeArcs(mat))
    mat_incidence = np.empty((ligne,colonne))
    arc = listeArcs(mat)
    
    
    for index_l in range(ligne):
        for indice, val in enumerate(arc):
            if index_l == indice  and (index_l,indice) == val:
                mat_incidence[index_l,indice] = 0
            elif index_l in val:
                mat_incidence[index_l,indice] = 1
            else:
                mat_incidence[index_l,indice] = 0
        
                     
               
    return mat_incidence
print("matriceIncidencer")
mat3 = np.array([[0,1,1,0,0],[0,0,1,0,1],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]])
print(listeArcs(mat3))
print("Matrice d'adjacence:")
print(mat3)
print("Matrice d'incidence:")
print(matriceIncidencer(mat3))
print("\n")

#7)fonction est voisin
def est_voisin(mat:object,S:int,V:int)->bool:

    if mat[S,V] == 1 or mat[V,S] == 1:
        res = True
    else:
        res = False
    return res

mat4 = np.array([[0,1,1,0,0],[0,0,1,0,1],[0,0,0,1,0],[0,0,0,0,1],[0,0,1,0,0]])
print("Matrice d'adjacence:")
print(mat4)
print(est_voisin(mat4,0,4))
print(est_voisin(mat4,3,4))