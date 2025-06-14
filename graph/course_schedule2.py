from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        for element in prerequisites:
            adj_list[element[1]].append(element[0])

        def isCyclic():
            visited = set()
            recursive = set()

            def dfs(node):
                if node in recursive:
                    return True
                
                if node in visited:
                    return False

                recursive.add(node)
                for n in adj_list[node]:
                    if dfs(n):
                        return True
                recursive.remove(node)
                visited.add(node)
                return False

            for v in range(numCourses):
                if dfs(v):
                    return True
            return False

        if isCyclic():
            return []

        def toposort():
            stack = []
            visited = set()

            def dfs(node):
                visited.add(node)
                for n in adj_list[node]:
                    if n not in visited:
                        dfs(n)
                stack.append(node)

            for v in range(numCourses):
                if v not in visited:
                    dfs(v)

            return stack[::-1]
        
        return toposort()


        