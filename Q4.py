def single_occurance( arr1):
    m = len(arr1) 
    ans = arr1[0]
     
    for i in range(1,m):
       ans = ans ^ arr1[i]
     
    return ans
 
arr1 = [7,7,8,2,9,5,4,5,4,9,2]
print ("Single Occurence :- ", single_occurance(arr1))