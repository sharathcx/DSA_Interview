from typing import List
grid = [[2,1,1],[1,1,0],[0,1,1]]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        queue = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        fresh = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        t=0
        
        while queue:
            r, c, t = queue.pop(0)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if rows>nr>=0 and columns>nc>=0 and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, t+1))
                    fresh -= 1
        return t if fresh == 0 else -1
s = Solution()
print(s.orangesRotting(grid))