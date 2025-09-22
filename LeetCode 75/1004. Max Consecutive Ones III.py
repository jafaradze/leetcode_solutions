from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = int(nums[0] == 0)
        i = j = 0
        res = 0
        while j < len(nums):
            if zeros <= k:
                j += 1
                if j < len(nums):
                    zeros += nums[j] == 0
            else:
                zeros -= nums[i] == 0
                i += 1
            res = max(res, j - i)
        return res