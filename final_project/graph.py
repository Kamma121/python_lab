class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def remove_edge(self, u, v):
        self.graph[u] = [(vertex, weight) for vertex, weight in self.graph[u] if vertex != v]

    def get_adjacent_vertices(self, u):
        return [v for v, w in self.graph[u]]

    def display_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}: ")
            for v, w in self.graph[i]:
                print(f" -> {v} (Weight: {w})")
