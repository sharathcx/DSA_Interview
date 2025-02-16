from typing import List
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        adj_list = {i:adj[i] for i in range(V)}
        visited = set()
        def dfs(start):
            stack = [(start, -1)]
            while stack:
                node, parent = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for n in adj_list[node]:
                        if n not in visited:
                            stack.append((n, node))
                        elif n != parent:
                            return True
            return False
        for node in range(V):
            if dfs(node):
                return True
            
        return False

sol = Solution()
V = 4
adj = [[1, 2], [0, 2], [0, 1, 3], [2]]  # Graph with a cycle (triangle)
print(sol.isCycle(V, adj))  # Output: True

adj2 = [[1], [0, 2], [1, 3], [2]]  # No cycle
print(sol.isCycle(V, adj2))  # Output: False

		

