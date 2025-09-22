from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s1 = 0
        s2 = 0
        for elem in nums:
            if elem < 10:
                s1 += elem
            else:
                s2 += elem
        return s1 != s2