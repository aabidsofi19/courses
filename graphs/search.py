
from graph import Graph, load_from_txt 
from collections import deque 

class BFS:
    
    def __init__(self,graph : Graph ,source ) :
        self.graph =  graph
        self.viewed = [False for _ in range(graph.v+1)]
        self.queue = deque()
        self.source = source 
        
        # index represent the vertex and value represent the parent 
        self.edge_to = [None for _ in range(graph.v+1)] 
    
        self.add_to_queue(source)
        self.viewed[source] = True 
    
        self.search()

    def is_visited(self,v) :
        return self.viewed[v]

    def add_to_queue(self,v) :
        self.queue.appendleft(v)
    
    def is_path_to(self,u) :
        """ run after doing a search using a source vertex """
        return self.viewed[u]

    def search(self) :
        
        while len(self.queue) != 0 :
            
            v = self.queue.popleft() 

            for w in self.graph.adj[v]  :
                if not self.is_visited(w) :
                    self.viewed[w] = True 
                    self.add_to_queue(w)
                    self.edge_to[w] = v 

    
    def path(self,v) :
        if not self.is_path_to(v) :
            return f"Path doesnt exist from {self.source} -> {v}" 
        
        print(f"Path from {self.source} {v}") 
        
        parent = self.edge_to[v]
        path = deque([str(v)]) 

        while parent :
            path.appendleft(str(parent))
            parent = self.edge_to[parent]
        
        return path
        

class DFS:
    
    def __init__(self,graph : Graph ,source ) :
        self.graph =  graph
        self.viewed = [False for _ in range(graph.v+1)]
        self.stack = deque([source])
        self.source = source 
        
        # index represent the vertex and value represent the parent 
        self.edge_to = [None for _ in range(graph.v+1)] 
    
        self.viewed[source] = True 
    
        self.search_iter()

    def is_path_to(self,u) :
        """ run after doing a search using a source vertex """
        return self.viewed[u]
    
    def search(self,s) :
        self.viewed[s] = True 

        for w in self.graph.adj[s] :
            if not self.viewed[w] :
                self.search(w) 
                self.edge_to[w] =  s 

    def search_iter(self) :
        
        while len(self.stack) != 0 :
            
            v = self.stack.pop() 

            for w in self.graph.adj[v]  :
                if not self.viewed[w] :
                    self.viewed[w] = True 
                    self.stack.append(w)
                    self.edge_to[w] = v 

    
    def path(self,v) :
        if not self.is_path_to(v) :
            return f"Path doesnt exist from {self.source} -> {v}" 
        
        print(f"Path from {self.source} {v}") 
        
        parent = self.edge_to[v]
        path = deque([str(v)]) 

        while parent :
            path.appendleft(str(parent))
            parent = self.edge_to[parent]
        
        return path
        
        
graph = load_from_txt("./small_graph.txt" , " ") 

bfs = DFS(graph,2)
print(bfs.path(4))
