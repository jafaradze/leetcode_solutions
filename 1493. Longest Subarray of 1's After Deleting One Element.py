from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        temp = ''.join(map(str, nums)).split('0')
        res = 0
        for i in range(len(temp) - 1):
            res = max(res, len(temp[i] + temp[i + 1]))
        return res
    

print(Solution().longestSubarray([1,1,0,1]))
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,1]))
