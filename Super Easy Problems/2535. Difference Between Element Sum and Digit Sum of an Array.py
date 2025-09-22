from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res1 = 0
        res2 = 0
        for elem in nums:
            res1 += elem
            res2 += sum(map(int, str(elem)))
        return abs(res1 - res2)