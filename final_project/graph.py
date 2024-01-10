class Graph:
    def __init__(self, vertices):
        self.edges = 0
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def v(self):
        return self.vertices

    def e(self):
        return self.edges

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.edges += 1

    def iternodes(self):
        return iter(self.graph)

    def iteredges(self):
        return ((u, v, w) for u, adj in self.graph.items() for v, w in adj)

    def remove_edge(self, u, v):
        self.graph[u] = [(vertex, weight) for vertex, weight in self.graph[u] if vertex != v]
        self.edges -= 1

    def get_adjacent_vertices(self, u):
        return (v for v, w in self.graph[u])

    def display_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}: ")
            for v, w in self.graph[i]:
                print(f" -> {v} (Weight: {w})")
