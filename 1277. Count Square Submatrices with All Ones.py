from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        temp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    temp[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    temp[i][j] = 1 + min(temp[i - 1][j], temp[i][j - 1], temp[i - 1][j - 1])
                res += temp[i][j]
        return res
    
print(Solution().countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
print(Solution().countSquares([[1,0,1],[1,1,0],[1,1,0]]))