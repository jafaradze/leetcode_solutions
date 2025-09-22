from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_ave = cur_sum / k
        for i in range(1, len(nums) - k + 1):
            cur_sum = cur_sum - nums[i - 1] + nums[i + k - 1]
            max_ave = max(max_ave, cur_sum / k)
        return max_ave
