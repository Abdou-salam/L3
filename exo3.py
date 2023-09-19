import random as rm
def choose_element_list(list_in_which_to_choose:list)->list:
    taille = len(list_in_which_to_choose) - 1
    if taille == -1:
        rep = None
    else:
        generer = rm.randint(0,taille)
        rep = list_in_which_to_choose[generer]
    return rep
lst_sorted=[i for i in range(10)]
print("Liste triée de départ",lst_sorted)
e1 = choose_element_list(lst_sorted)
print("A la première exécution",e1,"a été sélectionné")
e2 = choose_element_list(lst_sorted)
print('A la deuxième exécution',e2,'a été sélectionné')
assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l\'élément sélectionné est le même !"

#Exercice 4
print("partie exo4")
def extract_elements_list(list_in_which_to_choose,int_nbr_of_element_to_extract):
    lst = []
    for i in range(int_nbr_of_element_to_extract):
        elt = choose_element_list(list_in_which_to_choose)
        lst.append(elt)
    return lst
print("Liste de départ",lst_sorted)
sublist = extract_elements_list(lst_sorted,5)
print("La sous liste extraite est",sublist)
print("Liste de départ après appel de la fonction est",lst_sorted)
#lst_sorted = rm.sample()
