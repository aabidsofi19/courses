from graph import WeightedGraph, load_weighted_edges


def prims_mst(graph: WeightedGraph) -> WeightedGraph:
    """
    This function finds the minimum spanning tree of a weighted graph using
    Prim's algorithm.

    :param graph: WeightedGraph object representing the graph.
    :return: WeightedGraph object representing the minimum spanning tree of
    the graph.
    """
    # Initialize the algorithm with a source vertex
    source_vertex = 1
    # Keep track of the vertices that have already been spanned
    spanned_vertices = {source_vertex}
    # Get all vertices in the graph
    all_vertices = set(graph.vertices)
    # Create a new graph to represent the minimum spanning tree
    minimum_spanning_tree = WeightedGraph(graph.v)

    # Continue until all vertices have been spanned
    while spanned_vertices != all_vertices:
        # Get all edges that cross between the spanned vertices and the
        # unspanned vertices
        crossing_edges = [
            (u, v)
            for u in spanned_vertices
            for v in graph.adj[u]
            if v not in spanned_vertices
        ]
        # Find the edge with the smallest weight
        u, v = min(crossing_edges, key=graph.w.get)
        # Add the edge and its weight to the minimum spanning tree
        minimum_spanning_tree.add_edge(u, v, graph.w[(u, v)])
        # Add the newly spanned vertex to the set of spanned vertices
        spanned_vertices.add(v)

    # Return the minimum spanning tree
    return minimum_spanning_tree


def test(file_path: str, correct_cost: float) -> None:
    """
    This function tests the `prims_mst` function on a given graph file and
    expected minimum spanning tree cost.

    :param file_path: A string representing the path to the graph file.
    :param correct_cost: A float representing the expected minimum spanning
    tree cost.
    :return: None
    """
    # Print the name of the file being tested
    print(f"[+] Testing {file_path}")
    # Load the graph from the file
    graph = load_weighted_edges(file_path)
    # Find the minimum spanning tree of the graph
    mst = prims_mst(graph)
    # Calculate the cost of the minimum spanning tree
    cost = sum(mst.w.values())
    # Print the cost of the minimum spanning tree
    print("Cost of minimum spanning tree:", cost)
    # Check that the calculated cost matches the expected cost
    assert cost == correct_cost


if __name__ == "__main__":

    test("small_graph.testcase", 7)
    test("prim_2.testcase", 3)
    test("prims.testcase", 20934)
