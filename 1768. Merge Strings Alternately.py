class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        n, m = len(word1), len(word2)
        res = ''
        while i < n and j < m:
            res += word1[i] + word2[j]
            i += 1
            j += 1
        return res + word1[i:] + word2[j:]