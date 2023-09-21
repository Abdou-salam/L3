def est_triee(lst)->bool:
    taille = len(lst)
    rep =True
    i = 0
    while rep:
        if lst[i] < lst[i+1]:
            rep =True
            i += 1
        else:
            rep = False
    return rep



def stupid_sort(lst_to_sort:list)->list:
    taille = len(lst_to_sort)
    i = 0
    trie = True
    while not trie and i < taille:
