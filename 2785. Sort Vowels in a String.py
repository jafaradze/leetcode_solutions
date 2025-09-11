class Solution:
    def sortVowels(self, s: str) -> str:
        a = 'EUIOAeuioa'
        vow = sorted(filter(lambda x: x in a, s))
        res = []
        i = 0
        for char in s:
            if char in a:
                res.append(vow[i])
                i += 1
            else:
                res.append(char)
        return ''.join(res)
        

