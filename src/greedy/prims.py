from graph import WeightedGraph,load_weighted_edges
from dataclasses import dataclass


def prims_mst(graph:WeightedGraph) -> list:

    """ fast implementation of prims MST algorithm using Heap """

    s = 1 # source vertex to intialize the algorithm with 

    spanned = {s}
    V = set(graph.vertices)
    T = WeightedGraph(graph.v) 

    while spanned != V :

       crossing_edges = [ (u,v) for u in spanned for v in graph.adj[u] if v not in spanned ]
    #    print("crossing",crossing_edges)
       u,v = min(crossing_edges, key= graph.w.get )
    #    print("min",(u,v)) 
       T.add_edge(u,v , graph.w[(u,v)]) 
       spanned.add(v)

    return T 

       


def test(file,correct_cost)  :
    print(f"[+] testing {file}")
    graph = load_weighted_edges(file)
   #  print("graph",graph.adj,graph.w)
    mst = prims_mst(graph)
    cost =   sum(mst.w.values())
   #  print("mst" , mst.w) 
    print("cost of mst" , cost )
    assert cost == correct_cost


     
test("small_graph.testcase",7)
test("prim_2.testcase",3)
test("prims.testcase",20934)







