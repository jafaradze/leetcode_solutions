from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        dc = {}
        dr = {}
        n = len(grid)
        for i in range(n):
            temp = tuple(grid[i])
            dr[temp] = dr.get(temp, 0) + 1
            temp = tuple([row[i] for row in grid])
            dc[temp] = dc.get(temp, 0) + 1
        for k in dc:
            if k in dr:
                res += dc[k] * dr[k]
        return res
