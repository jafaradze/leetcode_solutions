from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n - 1, 1, -1):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0