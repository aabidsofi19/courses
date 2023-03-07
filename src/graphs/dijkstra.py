from graph import WeightedGraph,load_weighted_txt




def  find_shortest_path(graph : WeightedGraph , s :int ) :
    

    X = {s} 
    A = [float("+inf") for _ in range(graph.v+1)]
    A[s] = 0 
    V = {v for v in range(1,graph.v+1) if v != s } 
    def greedy_score(edge ) :
        v = edge[0]
        w = edge[1]
        return A[v] + graph.w[(v,w)] 

    while len(V) :
        print(X)
        print(V)
        # print(graph.adj[s])

        frontier_edges = ( (u,v) for u in X for v in graph.adj[u] if v not in X ) 
        # print(list(frontier_edges)) 
        v_ , w_ = min(frontier_edges,key= greedy_score )
        X.add(w_)
        V.remove(w_)
        A[w_] = greedy_score((v_,w_))

    return A
    
if __name__ == "__main__":
    
    gr = load_weighted_txt("./dijkstraData.testcase",separator="\t")
    # gr = load_weighted_txt("./small-dikstra.testcase") 
    # print("adj" , gr.adj)

    A = find_shortest_path(gr,1)
    # print("a",A)
    to_find = "7,37,59,82,99,115,133,165,188,197".split(",")

    to_find = map(int,to_find) 

    ans = [str(A[x]) for x in to_find]
    ans = ",".join(ans)
    print("ans",ans)

