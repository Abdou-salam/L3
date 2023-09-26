from operator import truediv
from sys import prefix


def mots_Nlettres(lst_mot:list,n)->list:
    res = []
    for val in lst_mot:
        if len(val) == n :
            res.append(val)
    return res
lst=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"]

print("teste 1")
print(mots_Nlettres(lst,5))

#2) Fonction commence_par
def commence_par(mot:str,prefixe:str)->bool:
        
    return prefixe == mot[0:len(prefixe)]


def test(mot,prefixe):
    if commence_par(mot,prefixe) == True:
        print("le mot {} commence par le prefixe {}".format(mot,prefixe))
    else:
          print("le mot ne {} commence pas par le prefixe {}".format(mot,prefixe))
             

print("")
print("Test  2")
mot = "bonjour"
prefixe = "bon" 
test(mot,prefixe)

def finit_par(mot,suffixe):
    taille = len(suffixe)
    fin = len(mot) 
    debut = len(mot) - taille
    res = False
    if suffixe == mot[debut:fin]:
        res =True
    return res

def test3(mot,suffixe):
    if finit_par(mot,suffixe) == True:
        print("le mot {} finit par le suffixe {}".format(mot,suffixe))
    else:
          print("le mot  {} ne se termine pas par le suffixe {}".format(mot,suffixe))
             

print("Test  3")
mot = "bonsoir"
suffixe ="soir"
test3(mot,suffixe)

#4)Fonction finissent_par
def finissent_par(lst_mot:list,suffixe:str)->list:
    liste = []
    for val in lst_mot :
        if finit_par(val,suffixe) == True:
            liste.append(val)
    return liste
print("teste question 4")
lst_mot = ["finir","salut","partir","pardonner","fuir","bonjour"]
suffixe ="ir"
print(finissent_par(lst_mot,suffixe))

#fonction commencent_par
def commencent_par(lst_mot,prefixe):
    lst = []
    for val in lst_mot :
        if commence_par(val,prefixe) == True:
            lst.append(val)
    return lst

print("teste question 5")
lst_mot = ["impossible","salut","calme","impot","imprimer"]
suffixe ="im"
print(commencent_par(lst_mot,suffixe))

#fonction liste_mots
def liste_mots(lst_mot,prefixe,suffixe,n):
    lst = []
    for val in lst_mot:
        if commence_par(val,prefixe) == True and finit_par(val,suffixe) == True and len(val) == n :
            lst.append(val)
    return lst

print("teste question 6")
lst_mot = ["infection","salut","inclinaison","impot","injection","parler","ingestion"]
prefixe ="in"
suffixe ="ion"
print(liste_mots(lst_mot,prefixe,suffixe,9))

#7 fonction dictionnaire
def dictionnaire(fichier:str)->list:
    lst = []
    f = open(fichier,"r")
    c = f.readline()
    while c != " " :
        lst.append(c)
    return lst

fichier = 'C:/Users/Etudiant/Desktop/Notes_de_cours/littreUTF8.txt'


print(commence_par(dictionnaire(fichier),"a"))





