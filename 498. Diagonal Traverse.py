from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i = j = 0
        dirs = ((-1, 1), (1, -1))
        dir = 0
        m, n = len(mat), len(mat[0])
        count = 0
        res = []
        while count != m * n:
            res.append(mat[i][j])
            count += 1
            if j == n - 1 and dir == 0:
                i += 1
                dir = (dir + 1) % 2
            elif i == m - 1 and dir == 1:
                j += 1
                dir = (dir + 1) % 2
            elif i == 0 and dir == 0:
                j += 1
                dir = (dir + 1) % 2
            elif j == 0 and dir == 1:
                i += 1
                dir = (dir + 1) % 2
            else:
                i += dirs[dir][0]
                j += dirs[dir][1]
        return res
    
print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().findDiagonalOrder([[1,2],[3,4]]))
print(Solution().findDiagonalOrder([[1]]))

