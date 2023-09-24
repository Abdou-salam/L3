def findMin(lst):
    mini = None
    if len(lst) == 0:
        return ValueError
    elif len(lst) == 1:
       mini = lst[0]
       return mini
    else:
        mini = findMin(lst[1:])
        print(mini)
        if mini > lst[0]:
            mini = lst[0]
    return mini

         
       
    
print("minimum")
print(findMin([1,3,4,8,3]))
print(findMin([]))
