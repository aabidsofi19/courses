
from graph import Graph,load_from_txt
import random 
import math
import copy 

graph = load_from_txt("./graph1.txt","\t") 


def min_cut_trial(graph:Graph) :
    
    shadow_graph = [[v] for v in range(graph.v+1)]

    for _ in range(graph.v - 2 ) :
        contract(graph,shadow_graph) 
    
    # print("shadown" , shadow_graph)
    # print([x for x in shadow_graph if x is not None ])
    return  len(max((x for x in graph.adj if x is not None ) ,key=len))


def min_cut(graph:Graph) :
     
    trials = ( graph.v ** 2 ) * int(math.log(graph.v)) # n^2 log n trials 
    print(f"running {trials} trials")
    min_so_far = float("inf")
    # print("graph",graph.adj)
    for i in range(200) :
        print("running",i)
        graph_ = Graph(graph.v) 
        graph_.adj = copy.deepcopy(graph.adj)
        new_min = min_cut_trial(graph_)
        min_so_far = min(min_so_far,new_min) 
    
    return min_so_far 
  

def contract(graph : Graph , shadow_graph ) : 
    edges = list(graph.edges())
    node_1 , node_2 = edges[random.randint(0,len(edges)-1)]
    
    # print(f"contracting {node_1} and {node_2}")
    # merge node_2 into node_1
    graph.adj[node_1].extend(graph.adj[node_2])

    # remove self loops 
    remove_all(graph.adj[node_1],node_1)
    remove_all(graph.adj[node_1],node_2) 
    
    #rename pointers to node_2 
    for i in  graph.adj[node_2] :
        replace_all(graph.adj[i] , node_2 , node_1 ) 
    
    graph.adj[node_2] = None 
    graph.v -= 1
    # print(graph.adj)
    #only needed if you need to get the constituting nodes for cut
    # shadow_graph[node_1].extend(shadow_graph[node_2] ) 
    # shadow_graph[node_2] = None 

  
   

def replace_all(arr,x,y) :
    for i, v in enumerate(arr) :
        if v == x :
            arr[i] = y 
    
def remove_all(arr,x) :
    try : 
        arr.remove(x)
        remove_all(arr,x) 
    except ValueError :
        return 


if  __name__ == "__main__":
    x = min_cut(graph) 
    print(x)
