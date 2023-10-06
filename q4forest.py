#Q4. Count number of trees in a forest.
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph
    def dfs(self, vertex, visited):
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)
    def count_trees_in_forest(self):
        visited = {vertex: False for vertex in self.graph}
        count = 0
        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs(vertex, visited)
                count += 1
        return count
g = Graph()
g.add_edge(0, 1)
g.add_edge(2, 3)
g.add_edge(4, 5)
g.add_edge(6, 7)
count = g.count_trees_in_forest()
print(f"Number of trees in the forest: {count}")
