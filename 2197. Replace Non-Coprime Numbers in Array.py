from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        from math import gcd
        stack = []
        for num in nums:
            while stack:
                cur_gcd = gcd(stack[-1], num)
                if cur_gcd == 1:
                    break
                num = stack.pop() * num // cur_gcd
            stack.append(num)
        return stack