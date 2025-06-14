from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = {i: graph[i] for i in range(len(graph))}
        visited = set()
        recursive = set()

        def dfs(node):
            
            if node in recursive:
                return True  # cycle detected
            if node in visited:
                return False  # already verified safe
            
            recursive.add(node)
            for neighbor in adj_list[node]:
                if dfs(neighbor):
                    return True
            recursive.remove(node)
            visited.add(node)
            return False  # safe node

        result = []
        for v in range(len(graph)):
            if not dfs(v):  # if not part of a cycle
                result.append(v)

        return sorted(result)

# Test
s = Solution()
print(s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
