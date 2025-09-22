class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = []
        v = 'eyuioaEYUIOA'
        oth = []
        cur = ''
        for i in range(len(s)):
            if s[i] in v:
                vow.append(s[i])
                oth.append(cur)
                cur = ''
            else:
                cur += s[i]
        oth.append(cur)
        res = ''
        vow.reverse()
        for i in range(len(vow)):
            res += oth[i] + vow[i]
        return res + oth[-1]
    
print(Solution().reverseVowels("IceCreAm"))
print(Solution().reverseVowels("leetcode"))