class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        res = sign * int(str(abs(x))[::-1])
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0

    
print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
print(Solution().reverse(-120))
print(Solution().reverse(1534236469))