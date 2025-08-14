from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i = j = 0
        dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dir_i = 0
        m = len(matrix)
        n = len(matrix[0])
        for _ in range(n * m):
            res.append(matrix[i][j])
            matrix[i][j] = ''
            i += dir[dir_i][0]
            j += dir[dir_i][1]
            if i == m or j == n or i == -1 or j == -1 or matrix[i][j] == '':
                i -= dir[dir_i][0]
                j -= dir[dir_i][1]
                dir_i = (dir_i + 1) % 4
                i += dir[dir_i][0]
                j += dir[dir_i][1]
        return res
