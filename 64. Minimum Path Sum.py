from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        temp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    temp[i][j] = grid[i][j]
                elif i == 0:
                    temp[i][j] = grid[i][j] + temp[i][j - 1]
                elif j == 0:
                    temp[i][j] = grid[i][j] + temp[i - 1][j]
                else:
                    temp[i][j] = min(temp[i - 1][j], temp[i][j - 1]) + grid[i][j]
        return temp[m - 1][n - 1]