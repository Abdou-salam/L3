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
    mini = None
    if len(lst) == 0:
        return ValueError
    elif len(lst) == 1:
       mini = lst[0]
       return mini
    else:
        mini = findMin(lst[1:])
        if mini > lst[0]:
            mini = lst[0]
    return mini

         
       
    
print("minimum")
print(findMin([1,3,4,8,3]))
print(findMin([]))

def listPaire(lst):

    taille = len(lst) - 1
        
    if len(lst) == 0:
        return lst
    elif lst[taille] % 2 == 0:
        return [lst[taille]] + listPaire(lst[0:taille])
    else:
        return  listPaire(lst[0:taille])
    
print("liste paire")  
print(listPaire([16,3,4,8,3]))
print(listPaire([]))

#2 ème méthode
def listPaire2(lst):
    if len(lst) == 0:
        return []
    if lst[0] % 2 == 0:
        
        return [lst[0]] + listPaire2(lst[1:])
    else:
        return listPaire2(lst[1:])
    
print("liste paire2")  
print(listPaire2([18,3,4,8,3]))
print(listPaire2([]))

def concat_list(lst):
    index_max = len(lst) - 1

    if index_max == -1:
        return []
    else:
        return lst[index_max] + concat_list(lst[0:index_max])
print("concaténation")
print(concat_list([[0,1],[2,3],[4],[6,7]]))
print(concat_list([[4,0],[3,0],[2,4],[2,4,7]]))
print(concat_list([]))

def concat_list2(lst):
    if len(lst) == 0:
        return []
    else:
        return lst[0] + concat_list2(lst[1:])
print("concate 2")
print(concat_list2([[0,1],[2,3],[4],[6,7]]))

def separe(lst:list)->tuple:
    
    if len(lst) == 0:
        return ([],[])
    elif lst[0] % 2 == 0:
        pairs ,impairs = separe(lst[1:])
        return ([lst[0]] + pairs,impairs)
    else:
        pairs ,impairs = separe(lst[1:])
        return ( pairs,[lst[0]] + impairs)
lst = [1,6,7,4,9,11,28]
print("fonction separe")
res =separe(lst)
print(res[0])
print(res[1])

#Autre méthode 
def separe2(lst,result=([],[])):
    if len(lst) == 0:
        return result
    elif lst[0] % 2 == 0:
        result[0].append(lst[0])
    else:
        result[1].append(lst[0])
    return separe2(lst[1:],result)

lst2 = [1,6,7,4,9,11,28]
print("fonction separe2")
res =separe2(lst2)
print(res[0])
print(res[1])
