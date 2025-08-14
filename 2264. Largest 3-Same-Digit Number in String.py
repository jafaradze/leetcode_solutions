class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        i = 0
        flag = False
        n = len(num)
        while i < n - 2:
            if num[i] == num[i + 1] == num[i + 2] and num[i] > res:
                flag = True
                res = num[i]
                i += 3
            else:
                i += 1
        return res * 3 if flag else ''
    

print(Solution().largestGoodInteger("6777133339"))
print(Solution().largestGoodInteger("2300019"))
print(Solution().largestGoodInteger("42352338"))