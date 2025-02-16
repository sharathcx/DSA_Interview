from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = {x+1:[] for x in range(len(isConnected))}
        for i, edges in enumerate(isConnected):
             for j, element in enumerate(edges):
                if element == 1:
                    adj_list[i+1].append(j+1)
        visited = set()
        count = 0

        def bfs(start):
            queue = [start]
            visited.add(start)
            while queue:
                node = queue.pop(0)
                for n in adj_list[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)
        for node in adj_list.keys():
            if node not in visited:
                bfs(node)
                count +=1
        return count

sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))