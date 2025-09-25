class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        sign = '-' if numerator * denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        res = [sign, str(numerator // denominator)]
        seen = {}
        r = numerator % denominator
        if r == 0:
            return ''.join(res)
        res.append('.')
        while r != 0:
            if r in seen:
                p = seen[r]
                return f'{''.join(res[:p])}({''.join(res[p:])})'
            seen[r] = len(res)
            r *= 10
            res.append(str(r // denominator))
            r %= denominator
        return ''.join(res)
            



print(Solution().fractionToDecimal(10, 2))
print(Solution().fractionToDecimal(-10, 2))
print(Solution().fractionToDecimal(10, -5))
print(Solution().fractionToDecimal(-10, -5))


print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(4, 9))
print(Solution().fractionToDecimal(4, 333))

