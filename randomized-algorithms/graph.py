
class Graph :
    
    def __init__(self,V) :
        self.v = V  
        
        self.adj = [[] for _ in range(V+1)]


    def add_edge(self,u,v) :

        self.adj[u].append(v)
        self.adj[v].append(u)

    def edges(self) :
        for u,vertices in enumerate(self.adj)  :
            if vertices == None :
                continue 

            for v in vertices : 
                yield (u ,v)
            



def flatten(iterable) :
    arr = [] 
    for x in iterable : 
        if isinstance(x,map) :
            arr.append(flatten(x)) 
        else :
            arr.append(x)
    return arr 

def load_from_txt(file : str , separator = " ") -> Graph :
    
    with open(file,"r") as f :
        
        data = f.readlines() 
        data = map(lambda r : map(int , r.strip().split(separator)) , data )   
        data = flatten(data) 

        G = Graph(len(data))
        for r in data :
            u = r[0]
            for v  in r[1:] :
                G.adj[u].append(v)        
        return G 
       
