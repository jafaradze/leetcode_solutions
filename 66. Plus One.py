from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if set(digits) == {9}:
            return [1] + [0] * len(digits)
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        return digits