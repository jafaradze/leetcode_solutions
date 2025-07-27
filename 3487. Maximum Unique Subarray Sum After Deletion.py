from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(x < 0 for x in nums):
            return max(nums)
        max_sum = 0
        seen = set()
        s = 0
        for i in range(len(nums)):
            if nums[i] in seen:
                s = 0
                seen = set()
            if nums[i] > 0:
                s += nums[i]
                seen.add(nums[i])
            max_sum = max(max_sum, s)
        return max_sum