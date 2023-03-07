from collections import deque
from graph import Graph,load_from_txt  


class TopologicalSort:
    
    def __init__(self,graph : Graph ) :
        
        self.graph =  graph
        self.viewed = [False for _ in range(self.graph.v+1)]

        
    def run(self) :
        
        self.curr_label  = self.graph.v 
        self.f = [None for _ in range(self.graph.v + 1)] 

        for v in range(self.graph.v+1) :

            if not self.viewed[v] :
                self.dfs(v)
       
        

    def dfs(self,s) :
        self.viewed[s] = True 

        for w in self.graph.adj[s] :
            if not self.viewed[w] :
                self.dfs(w)
        
        print("s",s,"f",self.curr_label)
        self.f[self.curr_label] = s  
        self.curr_label -= 1




graph= load_from_txt("./dag.txt"," ")

g = TopologicalSort(graph)
g.run()
print(g.f)
