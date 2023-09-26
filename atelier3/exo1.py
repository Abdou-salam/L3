# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:16:01 2023

@author: hp
"""
def full_name(str_arg:str)->str:
    compteur = 0
    for i in range(len(str_arg)):
        if str_arg[i] != " " :
            compteur += 1
        else:
            t = i + 1
            break
    return str_arg[0:compteur].upper() + " " + str_arg[t].upper()+str_arg[t+1:]

print(full_name("salam diallo"))
print(full_name("adiouma sow"))
print(full_name( "bisgambiglia paul"))

def recherche(lst:list,elt:str)->int:
    
    
    return rep

        
def is_mail(str_arg:str)->(int,int):
    taille = len(str_arg)
    position = 0
    for i in range(len(str_arg)):
        if "@" ==  str_arg[i] :
            position = i
        else:
            res = (0,2)
            break
       
    
        
    t = (position - 1)  
    if str_arg[0] == "." or str_arg[t] == ".":
        res = (0,1)
    elif  str_arg[position + 1] == "." or str_arg[-1] == ".":
        res = (0,3)
    else:
        for i in range (0,position - 1):
            if str_arg[i] == "." and str_arg[i+1] =="." :
                res = (0,1)
            else:
                valide1 = True
        for i in range (position +1,taille):
            if str_arg[i] == "." and str_arg[i+1] =="." :
                res = (0,3)
            else:
                valide2 = True
        if valide1 == True and valide2 == True:
            res = (1,1)
            
    return res
str_variable2test = "bisgambiglia_paul@univ-corse.fr"
is_mail(str_variable2test)
str_variable2test = "bisgambiglia_paulOuniv-corse.fr"
is_mail(str_variable2test)
str_variable2test = "bisgambiglia_paul@univ-corsePOINTfr"
is_mail(str_variable2test)
str_variable2test = "@univ-corse.fr"
is_mail(str_variable2test)

        
   
            
    
    

        
       