from typing import Literal
from graph import Graph 
from collections import deque

def load(file, n ) :
    gr = Graph(n)
    gr_rev = Graph(n)

    with  open(file, "r") as file :
        data = file.readlines()

    for line in data:
        u,v = map(int,line.split())
        gr.add_edge(u,v)
        gr_rev.add_edge(v,u)

    
    return gr , gr_rev 

 

class StrongComponents :
    
    def __init__(self,gr,gr_rev) :
        self.gr = gr
        self.gr_rev = gr_rev 
        self.num_nodes = self.gr.v 

        self.first_pass()
        self.second_pass()
        
    
    def first_pass(self) :
        
        self.viewed = [False for _ in range(self.gr_rev.v+1)] 
        self.stack = deque()

        # t is running count for finishing time 
        # i.e no of nodes processed in first pass 
        self.t = 0 
        
        # ordering of nodes order[t] = node 
        self.order = [0 for _ in range(self.gr_rev.v + 1)]

        for v in range(self.gr_rev.v,0,-1) :
            # print("v" ,v)
            if  not self.viewed[v] :
                self.dfs(self.gr_rev,v,1) 
    
    def second_pass(self) :
        
        self.viewed = [False for _ in range(self.gr.v+1)] 
        self.stack = deque()
       
        # maps size of scc for leader as index
        self.scc : list[int ]= [0 for _ in range(self.gr.v+1)] 

        # leader is the current source vertex for sccs
        self.leader = None

        # print("order",self.order)
        for v in reversed(self.order) :

            if not self.viewed[v] :
                self.leader =  v
                self.dfs(self.gr,v,2)


    def dfs(self,graph, s , pass_ ) :
        # print("dfs(",s,")") 
        self.viewed[s] = True 
        if pass_ == 2 :
            # print("leader",self.leader)
            self.scc[self.leader] +=1  

        for v in graph.adj[s] :
            if not self.viewed[v] :
                self.dfs(graph,v,pass_)
        
        if pass_ == 1 :
            self.t += 1
            # print("finised " , s , "in " , self.t)
            self.order[self.t] = s 

        
if  __name__ == "__main__":
    
    ########################################################
    # Importing the graphs
    gr , gr_rev = load("./edges_small.txt",8)
    # print(gr.adj)
    # print(gr_rev.adj)
    scc = StrongComponents(gr,gr_rev)
    print(scc.scc)
    print(sorted(scc.scc[1:],reverse=True))
    # print(scc.order)
   
