# basic implementation of graph

class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj_list = {i:[] for i in vertex}
        self.edges = []

    def add_edge(self, u, v, w=0):
        self.adj_list[u].append((v,w))
        self.adj_list[v].append((u,w))
        self.edges.append((u,v,w))
        return True

    def bfs(self, start):
        visited = set(start)
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbour, _ in self.adj_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return result
    
    def dfs(self, start):
        visited = set(start)
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            result.append(node)
            for neighbour, _ in self.adj_list[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
        return result

    

graph = Graph(["A", "B", "C", "D"])
graph.add_edge("A", "B", 10)
graph.add_edge("B", "C", 50)
graph.add_edge("C", "D", 20)
graph.add_edge("A", "D", 70)
print(graph.adj_list)
print(graph.bfs("A"))
print(graph.dfs("A"))

    