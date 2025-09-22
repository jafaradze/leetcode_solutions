from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for s in hours:
            if s >= target:
                res += 1
        return res