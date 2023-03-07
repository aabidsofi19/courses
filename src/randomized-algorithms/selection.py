
from typing import List 


def swap(arr,i,j) :

    arr[i],arr[j] = arr[j] ,arr[i] 

def partition(arr,l,r) :
    p = arr[l] 
    i = l+1 
    for j in range(l+1,r+1) :
        if arr[j] < p :
            swap(arr,i,j)
            i+=1 
    swap(arr,l,i-1)
    return i-1 


def select(arr : List[int] , order , l , r )  : 
    if r <= l :
        return arr[l] 

    j= partition(arr,l,r)

    if j < order : 
        return select(arr,order-j,j+1,r)
    if j > order :
        return select(arr,order,l,j-1) 
    return arr[j]

def select_order(arr,order) :
    if order > len(arr) or order < 0 :
        raise ValueError("Invalid value for order statistic")
    return select(arr , order , 0 ,len(arr) -1 )

if  __name__ == "__main__":
    arr = [1,2,3,4,5,4,2,55,3,5,2,44,1,3,5]
    print(select_order(arr,0))
    print(arr)



