class Graph:
    def __init__(self, vertices):
        self.adj_list = {i:[] for i in vertices}
        self.edges = []

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v,w))
        # self.adj_list[v].append((u,w))
        self.edges.append((u,v,w))

    def bfs(self, start):
        visited = set(start)
        result = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            result.append(node)
            for n , _ in self.adj_list[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

        return result
    
    def dfs(self, start):
        visited = set(start)
        result = []
        stack = [start]

        while stack:
            node = stack.pop()
            result.append(node)
            for n, _ in self.adj_list[node]:
                if n not in visited:
                    visited.add(n)
                    stack.append(n)
        
        return result
    
    def topo_sort(self):
        stack = []
        visited = set()

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
    
    def is_cyclic(self):
        visited = set()
        recursive = set()

        def dfs(node):
            if node in recursive:
                return True
            if node in visited:
                return False
            
            recursive.add(node)
            for n, _ in self.adj_list[node]:
                if dfs(n):
                    return True

            recursive.remove(node)
            visited.add(node)
            return False
        
        for v in self.adj_list.keys():
            if dfs(v):
                return True
            
        return False



graph = Graph(["A", "B", "C", "D"])
graph.add_edge("A", "B", 10)
graph.add_edge("B", "C", 50)
graph.add_edge("C", "D", 20)
graph.add_edge("A", "D", 70)
graph.add_edge("D", "A", 5)

print(graph.bfs('A'))
print(graph.dfs("A"))
print(graph.topo_sort())
print(graph.is_cyclic())