class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        d = Counter(s)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1