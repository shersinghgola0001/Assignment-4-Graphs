#Q2. Depth First Traversal for a Graph.

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def dfs(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)
    def depth_first_traversal(self, start_vertex):
        visited = [False] * len(self.graph)
        self.dfs(start_vertex, visited)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal (starting from vertex 2):")
g.depth_first_traversal(2)
