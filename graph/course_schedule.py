from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for element in prerequisites:
            adj_list[element[1]].append(element[0])
        
        visited = set()
        recursive_set=set()
        def isCyclic(node):
            if node in recursive_set:
                return True
            
            if node in visited:
                return False
            
            recursive_set.add(node)
            for n in adj_list[node]:
                if isCyclic(n):
                    return True
                
            recursive_set.remove(node)
            visited.add(node)
            return False
        

        for v in range(numCourses):
            if isCyclic(v):
                return False
            
        return True



s = Solution()
print(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
