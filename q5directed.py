#Q5. Detect Cycle in a Directed Graph.

from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def is_cyclic_util(self, vertex, visited, rec_stack):
        visited[vertex] = True
        rec_stack[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[vertex] = False
        return False
    def is_cyclic(self):
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices
        for vertex in range(self.vertices):
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, rec_stack):
                    return True
        return False
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

if g.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
