class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def temp(s, n):
            if s == n:
                return 1
            elif s > n:
                return 0
            return temp(s + 1, n) + temp(s + 2, n)
        return temp(0, n)