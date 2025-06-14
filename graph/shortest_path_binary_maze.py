from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if (grid[0][0] != 0) or (grid[n-1][n-1] != 0):
            return -1
        directions = [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        queue = [(0, 0, 1)]
        grid[0][0] = 1
        while queue:
            x, y, d = queue.pop(0)
            if (x == n-1) and (y == n-1):
                return d

            for dr, dc in directions:
                nx, nc = dr + x, dc + y
                if (0<=nx<n) and (0<=nc<n) and (grid[nx][nc] == 0):
                    queue.append((nx, nc, d+1))
                    grid[nx][nc] = 1

        return -1