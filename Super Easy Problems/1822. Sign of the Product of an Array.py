from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        from math import prod
        res = prod(nums)
        if res > 0:
            return 1
        elif res < 0:
            return -1
        else:
            return 0