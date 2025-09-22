class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = 'aouie'
        cur_vow = sum(1 for char in s[0:k] if char in vow)
        res = cur_vow
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vow:
                cur_vow -= 1
            if s[i + k - 1] in vow:
                cur_vow += 1
            res = max(res, cur_vow)
        return res