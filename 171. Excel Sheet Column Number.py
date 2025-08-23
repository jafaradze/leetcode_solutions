class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        from string import ascii_uppercase

        res = 0
        n = len(columnTitle)
        for i in range(len(columnTitle)):
            res += 26 ** (n - i - 1) * (ascii_uppercase.index(columnTitle[i]) + 1)
        return res
    
print(Solution().titleToNumber('A'))
print(Solution().titleToNumber('AB'))
print(Solution().titleToNumber('ZY'))

