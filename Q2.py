def intersection(lst1 ,lst2):
    return(set(lst1)&set(lst2))


lst1 = [7,2,7,9,5,7,8,10,11,545]
lst2 = [9,4,9,8,4]
print(intersection(lst1 ,lst2))