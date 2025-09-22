from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [candies[i] + extraCandies >= max(candies) for i in range(len(candies))]
    

print(Solution().kidsWithCandies([2,3,5,1,3], 3))
print(Solution().kidsWithCandies([4,2,1,1,2], 1))