from dataclasses import dataclass , field
from typing import Any, Dict, List , Optional
import math

@dataclass(order=True) 
class PriortisedItem :
    value : Any = field(compare=False)
    key : int 
def coalese(x : Optional[Any] , y : Optional[Any]) -> Optional[Any] :
    """Returns the first none None if exists"""
    if x is None :
        return y
    return x

class Heap :

    def __init__(self,arr) -> None:
        
        self.heap : List[PriortisedItem] = [PriortisedItem(None,0)]
        self.map : Dict[int,int] = {} #stores the mapping of keys to array index 

        for k in arr :
            self.insert(k,k)
    
    def swap(self,i,j) :

        self.heap[i] , self.heap[j]  = self.heap[j] , self.heap[i]
        self.map[self.heap[i].key] , self.map[self.heap[j].key]  = j , i

    @property
    def size(self) :
        return len(self.heap) - 1
        
    def insert(self,key,value) :
        self.heap.append(PriortisedItem(value,key))
        self.map[key] = self.size 
        self.bubble_up(self.size)
    
    def delete(self,node:int)   : 
        """deletes node by index in heap array"""
        
        if self.size < node :
            raise Exception("Heap Underflow")
        

        del self.map[self.heap[node].key]
        
        if self.size == node :
            return self.heap.pop()

        min_ = self.heap[node]
        
        self.heap[node] = self.heap.pop() # replace the root with last leaf 
        self.map[self.heap[1].key] = 1 

        self.bubble_down(node)

        return min_

    def extract_min(self ) :
        return self.delete(1) 
        

    def parent(self,i) -> Optional[int]:
        if i == 1 :
            return None # no parent for root node 
        return math.floor(i/2)  
    
    def leftChild(self,i) -> Optional[int] :

        v = 2*i
        if v > self.size :
            return None 
        return v
    

    def min_child(self,i:int) -> Optional[int] :
        """returns the min child of a node if exists"""
        
        left  = self.leftChild(i) 
        right = self.rightChild(i) 
        
        if left is None or right is None :
            return coalese(left,right)

        return min(left,right , key=self.heap.__getitem__)



    def rightChild(self,i) -> Optional[int]:
        v = 2*i + 1
        if v > self.size :
            return None 
        return v

    def bubble_up(self,node : int ) :
        parent = self.parent(node) 
        if not parent :
            return
        
        parent_item = self.heap[parent]
        node_item = self.heap[node] 

        if node_item < parent_item :
            self.swap(node,parent)
            self.bubble_up(parent)

    def bubble_down(self,node : int ) :
        min_child = self.min_child(node)
        if min_child is None :
            return 

        if self.heap[min_child] < self.heap[node] :
            self.swap(node,min_child)
            self.bubble_down(min_child)
    
    def peek(self) :
        return self.heap[1] 


    def __repr__(self) -> str:
        return repr(self.heap[1:])
        

class MaxHeap(Heap) :
    
    def insert(self, key, value):
        return super().insert(-1 * key, value)

    def extract_max(self) :
        return super().extract_min()


if __name__ == "__main__":
    l = [10 , 4,4,9,11,13,12,9,8]
    h = MaxHeap(l)
    l = Heap(l)
   
    print("deleted" , l.delete(5)) 
    while l.size > 0 :
       print("min",l.extract_min())

    while h.size > 0 :
        print("max",h.extract_max()) 
    



