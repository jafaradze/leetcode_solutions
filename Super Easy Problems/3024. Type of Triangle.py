from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return 'equilateral'
            elif a == b or a == c or b == c:
                return 'isosceles'
            else:
                return 'scalene'
        else:
            return 'none'