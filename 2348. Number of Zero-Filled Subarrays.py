from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = [int(nums[0] == 0)]
        for i in range(1, len(nums)):
            res.append(res[-1] + 1 if nums[i] == 0 else 0)
        return sum(res)
    

print(Solution().zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(Solution().zeroFilledSubarray([0,0,0,2,0,0]))
print(Solution().zeroFilledSubarray([2,10,2019]))