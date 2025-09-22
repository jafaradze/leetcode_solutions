from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 1 if arr[0] % 2 == 1 else 0
        for i in range(1, len(arr)):
            if arr[i] % 2 == 1 and arr[i - 1] % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 1
        return True if count == 3 else False