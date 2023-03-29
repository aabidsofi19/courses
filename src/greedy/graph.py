

class Graph:

    def __init__(self, V):

        self.v = V
        self.adj = [[] for _ in range(V+1)]

    @property
    def vertices(self):
        return (v for v in range(1, self.v+1))

    def add_edge(self, u, v):

        self.adj[u].append(v)
        # self.adj[v].append(u)

    def edges(self):
        for u, vertices in enumerate(self.adj):
            if vertices == None:
                continue

            for v in vertices:
                yield (u, v)


class WeightedGraph(Graph):

    def __init__(self, V):

        super().__init__(V)
        self.w = {}

    def add_edge(self, u, v, w):
        self.w[(u, v)] = w
        return super().add_edge(u, v)


def flatten(iterable):
    arr = []
    for x in iterable:
        if isinstance(x, map):
            arr.append(flatten(x))
        else:
            arr.append(x)
    return arr


def load_from_txt(file: str, separator=" ") -> Graph:
    """loads a graph from an adjancency list representation"""
    with open(file, "r") as f:

        data = f.readlines()
        data = map(lambda r: map(int, r.strip().split(separator)), data)
        data = flatten(data)

        G = Graph(len(data))
        for r in data:
            u = r[0]
            for v in r[1:]:
                G.adj[u].append(v)

        return G


def load_weighted_edges(file: str, separator=" ", w_separator=" ") -> WeightedGraph:
    """loads a graph from edges as v separator u w_separator weight"""

    with open(file, "r") as f:

        data = f.readlines()
        v,e =  map(int,data[0].split(" "))

        data = map(lambda line: line.strip().split(separator), data[1:])
        data = flatten(data)
        # print("data",data)
        G = WeightedGraph(v)

        for r in data:
            # print(r)

            u, v, weight = map(int, r)
            G.adj[u].append(v)
            G.w[(u, v)] = weight

            G.adj[v].append(u)
            G.w[(v,u)]=weight


        return G


def load_weighted_txt(file: str, separator=" ") -> WeightedGraph:
    """loads a graph from an adjancency list representation"""
    with open(file, "r") as f:

        data = f.readlines()
        data = map(lambda line: line.strip().split(separator), data)
        data = flatten(data)
        # print("data",data)
        G = WeightedGraph(len(data))

        for r in data:
            # print(r)
            u = int(r[0])

            for edge in r[1:]:
                v, weight = map(int, edge.strip().split(","))
                G.adj[u].append(v)
                G.w[(u, v)] = weight
        return G
