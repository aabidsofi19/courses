from ..graphs.graph import WeightedGraph
from ..datastructures.heap import Heap 

def prim(graph : WeightedGraph ) :
    
    #intialization
    s = 1
    X = {s}
    MST = [] 
    
    remaining = X - set(range(1,graph.v+1)) 

    heap =  Heap([])
    
    # intializing the heap with costs  
    for v in remaining  :

        min_cost = float("inf") 
        if v in graph.adj[1] :
            min_cost = graph.w[(1,v)]
        heap.insert(min_cost,(s,v)) 

    while remaining :
       
        u,v =  heap.extract_min().value 
        
        X.add(v) 
        remaining.remove(v) 
        MST.append((u,v))
        
        for w in graph.adj[v] :
           pass 
        
     
    


  
