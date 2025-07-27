from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new_nums = [nums[0]]
        for elem in nums[1:]:
            if elem != new_nums[-1]:
                new_nums.append(elem)

        count = 0
        for i in range(1, len(new_nums) - 1):
            if new_nums[i - 1] > new_nums[i] < new_nums[i + 1] or \
            new_nums[i - 1] < new_nums[i] > new_nums[i + 1]:
                count += 1
        return count