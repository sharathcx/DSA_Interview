from typing import List
image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        origin = image[sr][sc]
        image[sr][sc] = color
        rows, columns = len(image), len(image[0])
        queue = [(sr, sc)]
        visited = set((sr, sc))
        while queue:
            r, c = queue.pop(0)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<columns and image[nr][nc] == origin:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        image[nr][nc] = color
                        queue.append((nr, nc))
        return image
    
s = Solution()
print(s.floodFill(image, sr, sc, color))
