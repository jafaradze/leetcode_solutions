class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        cur = res = ''
        i = 0
        n, m = len(str1), len(str2)
        while i < n and i < m:
            cur = str1[:i + 1]
            if (n // len(cur) * cur == str1) and (m // len(cur) * cur == str2):
                res = max(res, cur, key=len)
            i += 1
        return res
