from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        i = j = 0
        dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dir_i = 0
        for a in range(1, n ** 2 + 1):
            res[i][j] = a
            i += dir[dir_i][0]
            j += dir[dir_i][1]
            if i == n or j == n or i == -1 or j == -1 or res[i][j] != 0:
                i -= dir[dir_i][0]
                j -= dir[dir_i][1]
                dir_i = (dir_i + 1) % 4
                i += dir[dir_i][0]
                j += dir[dir_i][1]
        return res

