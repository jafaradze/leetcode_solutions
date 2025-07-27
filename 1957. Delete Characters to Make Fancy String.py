class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        cur_count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_count += 1
            else:
                cur_count = 1
            if cur_count < 3:
                res += s[i]
        return res