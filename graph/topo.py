# basic implementation of graph

class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj_list = {i:[] for i in vertex}
        self.edges = []

    def add_edge(self, u, v, w=0):
        self.adj_list[u].append((v,w))
        # self.adj_list[v].append((u,w))
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


    def topo_sort(self):
        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)
            for n, _ in self.adj_list[node]:
                if n not in visited:
                    dfs(n)
            stack.append(node)

        for v in self.adj_list.keys():
            if v not in visited:
                dfs(v)

        return stack[::-1]


    

graph = Graph(["T1", "T2", "T3", "T4", "T5", "T6"])

# Adding dependencies (edges)
graph.add_edge("T1", "T2")
graph.add_edge("T1", "T3")
graph.add_edge("T3", "T4")
graph.add_edge("T2", "T4")
graph.add_edge("T4", "T5")
graph.add_edge("T5", "T6")
print(graph.adj_list)
print(graph.bfs("T1"))
print(graph.dfs("T1"))
print(graph.topo_sort())


    