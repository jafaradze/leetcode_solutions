class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from math import prod
        return prod(map(int, str(n))) - sum(map(int, str(n)))