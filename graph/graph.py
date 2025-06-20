# basic implementation of graph
from heapq import heappop, heappush
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
    

    def dijkstra(self, start):
        dist = {i : float('inf') for i in self.vertex}
        heapq = [(0,start)]
        dist[start] = 0
        visited = set()
        while heapq:
            d, node = heappop(heapq)
            if node not in visited:
                visited.add(node)
                for n, w in self.adj_list[node]:
                    temp_d = d + w
                    if temp_d < dist[n]:    
                        dist[n] = temp_d
                        heappush(heapq, (temp_d, n))

        return dist
    
    def bellman(self, start):
        dist = {i : float('inf') for i in self.vertex}
        dist[start] = 0
        for i in range(len(self.vertex)-1):
            for u, v, w in self.edges:
                temp = dist[u] + w
                if temp < dist[v]:
                    dist[v] = temp

        return dist



    
                
    






    
graph = Graph(["A", "B", "C", "D"])
graph.add_edge("A", "B", 10)
graph.add_edge("B", "C", 50)
graph.add_edge("C", "D", 20)
graph.add_edge("A", "D", 70)

print(graph.vertex)
print("Adjacency List:", graph.adj_list)
print("BFS:", graph.bfs("A"))
print("DFS:", graph.dfs("A"))
print("Dijkstra from A:", graph.dijkstra("A"))
print("Belman from A:", graph.bellman("A"))


    