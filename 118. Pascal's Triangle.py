from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            r = [1] * (i + 1)
            for j in range(i + 1):
                if j != 0 and j != i:
                    r[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(r)

        return res