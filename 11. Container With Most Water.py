from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        max_area = 0
        while i != j:
            left = height[i]
            right = height[j]
            cur_area = (j - i) * min(left, right)
            max_area = max(max_area, cur_area)
            if left < right:
                i += 1
            else:
                j -= 1
        return max_area
    
