from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_x = max_y = -1
        min_x, min_y = m, n
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_x = min(min_x, j)
                    min_y = min(min_y, i)
                    max_x = max(max_x, j)
                    max_y = max(max_y, i)
        return (max_x - min_x + 1) * (max_y - min_y + 1)
    
print(Solution().minimumArea([[0,1,0],[1,0,1]]))
print(Solution().minimumArea([[1,0],[0,0]]))