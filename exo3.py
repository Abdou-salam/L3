import random as rm
import time
from math import *

def gen_list_random_int(int_nbr =0,int_binf=0,int_bsup=0):
    if int_nbr == 0 and int_binf == 0 and int_bsup==0:
        lst = [ floor(rm.random()*(10 - 0)) for _ in range(10)]
    else:
        lst =[  floor(rm.random()*(int_bsup - int_binf)+ int_binf) for _ in range(int_nbr)]
    return lst    
print(gen_list_random_int(5,13,32))
print(gen_list_random_int())

def mix_list_v2(list_to_mix:list):
    ans = []
    fin = False
    i = 0
    while not fin:
        j = floor(rm.random()*(len(list_to_mix)))
        if  list_to_mix[j] != None:
            ans.append(list_to_mix[j])
            list_to_mix[j] = None
            i += 1
        if i == len(list_to_mix):
            fin = True

    return ans

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

def perf_mix(mix_list_v:callable,shuffle:callable,lst_int,nbr_ex)->tuple:
    res = ([],[])

    for  i in lst_int:
        diff1 = 0
        diff2 = 0

        for j in range(nbr_ex):
            lst= gen_list_random_int(i,0,100000)
            start = time.perf_counter()
            mix_list_v2(lst)
            end = time.perf_counter()
            diff1 += end-start

            start2 = time.perf_counter()
            shuffle(lst)
            end2 = time.perf_counter()
            diff2 += end2-start2

        res[0].append(diff1/nbr_ex)
        res[1].append(diff2/nbr_ex)
    return res


res = perf_mix(mix_list_v2,rm.shuffle,[10, 500, 5000, 50000, 100000],nbr_ex=5)
print(res[0])
print(res[1])
        
    