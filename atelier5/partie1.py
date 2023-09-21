def somme_recursive(lst):
    taille = len(lst) - 1
    
    
    if  len(lst) != 0:
        return lst[taille] + somme_recursive(lst[:taille - 1])   
    else:
        return 0 
    
# autre methode
def somme (lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + somme (lst[1:])

     
print(somme_recursive([1,3,4]))
print(somme([1,3,4]))

def factorielle_recursive(nbr):

    if nbr == 0:
        return 1
    else:
        return nbr *  factorielle_recursive(nbr-1)

print(factorielle_recursive(4))

def longueur(lst):
    taille = len(lst) -1
    if len(lst) == 0:
        return 0
    else:
        return 1 + longueur(lst[0:taille])
print("longueur")
print(longueur([1,3,4])),
print(longueur([1,3,4,8,3]))

def findMin(lst):

    if l