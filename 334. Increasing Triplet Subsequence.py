from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float('inf')
        for k in nums:
            if k > j:
                return True
            if k <= i:
                i = k
            else:
                j = k
        return False