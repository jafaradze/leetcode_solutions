from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        suf = 1
        for i in range(n - 1, -1, -1):
            pref[i] *= suf
            suf *= nums[i]
        return pref


print(Solution().productExceptSelf([1, 2, 3, 4]))