
import time
import exo1
def sort_list(lst:list)->list:
    taille =len(lst)
    lst2 =list(lst)
    lst3 =[]
    
    for i in range(taille):
       min_index = i
       for j in range(i,taille):
        if lst[min_index] > lst2[j]:
            min_index = j

       lst2[i],lst2[min_index] = lst2[min_index],lst2[i] 
       lst3.append(lst2[i])
    return lst3
     
lst =[4,9,12,1,56,6,102]
print(sort_list(lst))
print(sorted(lst))

def comparaison_sort_list(sort_list:callable,f_sorted:callable,list_taille:list,gen_list_random_int:list)->tuple:
    res = ([],[])
   
    for val in list_taille:
    #Premier tri avec sort_list
        lst = gen_list_random_int(val,0,1000000)
        start = time.perf_counter()
        sort_list(lst)
        end = time.perf_counter()
        diff1 = start - end
        # deuxieme tri avec la fonction sorted
        res[0].append(diff1)
        start2 = time.perf_counter()
        f_sorted(lst)
        end2 = time.perf_counter()
        diff2 = start2 - end
        res[1].append(diff2)
    return res
print(comparaison_sort_list(sort_list,sorted,[10, 500, 5000, 50000, 100000],exo1.gen_list_random_int))