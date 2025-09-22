from typing import List

# 1
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        temp = ''.join(map(str, nums)).split('0')
        res = 0
        for i in range(len(temp) - 1):
            res = max(res, len(temp[i] + temp[i + 1]))
        return res
    
# 2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        zeros = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            while zeros > 1:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            res = max(j - i, res)
        return res