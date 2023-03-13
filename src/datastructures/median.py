"""
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications).  
The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one.

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits).  
That is, you should compute (m1+m2+m3+⋯+m10000) mod 10000(m1​+m2​+m3​+⋯+m10000​)mod10000.

"""

from typing import Iterable
from heap import Heap,MaxHeap 



def add_number(lowes : MaxHeap ,highes : Heap, num : int) :
    
    if lowes.size == 0 or num < lowes.peek().value :
        lowes.insert(num,num)
    else :
        highes.insert(num,num) 


def rebalance(lowes : MaxHeap , highes : Heap ) :
    
    if lowes.size >  highes.size + 1 :
        x = lowes.extract_max().value 
        highes.insert(x,x) 

    if highes.size > lowes.size + 1:
        x = highes.extract_min().value 
        lowes.insert(x,x)


def get_median(lowes:MaxHeap , highes : Heap ) : 
   
    if lowes.size == highes.size : # thats n is even 
        return lowes.peek().value 
    
    # odd case 

    bigger_heap = max(lowes,highes,key=lambda h : h.size )
    return bigger_heap.peek().value



def running_median(input:Iterable[int]) -> list[int] :
    
    A = []
    
    lowes = MaxHeap([])
    highes = Heap([]) 

    for num in input : 
        
        add_number(lowes,highes,num) 
        rebalance(lowes,highes)
        m = get_median(lowes,highes)
        # print(lowes.heap)
        # print(highes.heap)
        A.append(m)
    
    return A
        
        
if __name__ == "__main__":
    
    with open("./medianMaintanence.testcase") as f :
          big_input = ( int(l.strip()) for l in f.readlines() )
    
    input = [1,666, 10 , 667 ,100 , 2 ,3]
    input_2 = [6331,2793,1640,9290,225,625,6195,2303,5685,1354]
    

    a = running_median(big_input)

    print(sum(a) % 10000)
