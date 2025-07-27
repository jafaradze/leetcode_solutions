from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        max_score = 0
        cur_score = 0
        seen = set()

        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                cur_score -= nums[l]
                l += 1
            seen.add(nums[r])
            cur_score += nums[r]
            max_score = max(max_score, cur_score)

        return max_score