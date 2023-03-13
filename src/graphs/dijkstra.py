import heapq
from graph import WeightedGraph,load_weighted_txt


def greedy_score(dist : list[int] , graph:WeightedGraph , edge ) :
        v = edge[0]
        w = edge[1]
        return dist[v] + graph.w[(v,w)] 



def  find_shortest_path(graph : WeightedGraph , s :int ) :
    
    X = {s}
    dist = [float("+inf") for _ in range(graph.v+1)]
    dist[s] = 0 
    # V = {v for v in range(1,graph.v+1) if v != s } 
    greedy_score_ = lambda edge  : greedy_score(dist ,graph,edge)

    while len(X) < graph.v  :
        print(X)
        frontier_edges = ( (u,v) for u in X for v in graph.adj[u] if v not in X ) 
        v_ , w_ = min(frontier_edges,key= greedy_score_ )
        X.add(w_)
        # V.remove(w_)
        dist[w_] = greedy_score_((v_,w_))

    return dist

"""
## Using a priority queue
A min-priority queue is an abstract data type that provides 3 basic operations: add_with_priority(), decrease_priority() and extract_min(). As mentioned earlier, using such a data structure can lead to faster computing times than using a basic queue

1  function Dijkstra(Graph, source):
2      dist[source] ← 0                           // Initialization
3
4      create vertex priority queue Q
5
6      for each vertex v in Graph.Vertices:
7          if v ≠ source
8              dist[v] ← INFINITY                 // Unknown distance from source to v
9              prev[v] ← UNDEFINED                // Predecessor of v
10
11         Q.add_with_priority(v, dist[v])
12
13
14     while Q is not empty:                      // The main loop
15         u ← Q.extract_min()                    // Remove and return best vertex
16         for each neighbor v of u:              // Go through all v neighbors of u
17             alt ← dist[u] + Graph.Edges(u, v)
18             if alt < dist[v]:
19                 dist[v] ← alt
20                 prev[v] ← u
21                 Q.decrease_priority(v, alt)
22
23     return dist, prev

"""
    
if __name__ == "__main__":
    
    gr = load_weighted_txt("./dijkstraData.testcase",separator="\t")
    # gr = load_weighted_txt("./small-dikstra.testcase") 
    # print("adj" , gr.adj)

    dist = find_shortest_path(gr,1)
    # print("a",dist)
    to_find = "7,37,59,82,99,115,133,165,188,197".split(",")

    to_find = map(int,to_find) 

    ans = [str(dist[x]) for x in to_find]
    ans = ",".join(ans)
    print("ans",ans)

