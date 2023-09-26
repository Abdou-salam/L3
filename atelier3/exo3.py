def places_lettre(ch:str,mot:str)->list:
    lst = []
    taille = len(mot) 
    for i in range (taille):
        if mot[i] == ch :
            lst.append(i)
    return lst
print("Teste de la fonction places_lettre")
print(places_lettre('b','bonjour'))
print(places_lettre('a','bonjour'))
print(places_lettre('m','maman'))

def test():
    mot = input("donner un mot:")
    ch = input("donner un caractere:")
    print(places_lettre(ch,mot))

test()

#Question 2

def outputStr(mot:str,lpost:list)->str:
    taille = len(mot)
    res = ""
    for i in range(taille):
        if len(lpost) == 0:
            res = res + "_ "
        else:
            res = res + mot[i]

    return res

print(outputStr("bonjour",[]))
print(outputStr("bonjour",[0]))