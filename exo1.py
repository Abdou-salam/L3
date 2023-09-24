from math import *
from random import *
def gen_list_random_int(int_nbr =0,int_binf=0,int_bsup=0):
    if int_nbr == 0 and int_binf == 0 and int_bsup==0:
        lst = [ floor(random()*(10 - 0)) for _ in range(10)]
    else:
        lst =[  floor(random()*(int_bsup - int_binf)+ int_binf) for _ in range(int_nbr)]
    return lst    
print(gen_list_random_int(5,13,32))
print(gen_list_random_int())

