
def binary_search(arr:list[int],t:int) -> int :
    
    left = 0
    right = len(arr) - 1 
    
    # if right == 0 :
    #    return 0  if arr[right] == t else - 1 
    # if right == -1 :
    #     return -1 
    #
    while left <= right :
        
        mid = (left + right) // 2
         
        print(left,right,mid)
        if arr[mid] == t :
            return mid 
        if arr[mid] < t : 
            left = mid + 1  
        else :
            right = mid -1

    return -1 




x = [1,2,3,4,5,6,7,8,9]
x = [0,10,20,30,40]
print(binary_search(x,40))

  
   
