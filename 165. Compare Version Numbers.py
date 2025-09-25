class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) > len(v2):
            for _ in range(len(v1) - len(v2)):
                v2.append(0)
        else:
            for _ in range(len(v2) - len(v1)):
                v1.append(0)
        for a, b in zip(v1, v2):
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        return 0
    
print(Solution().compareVersion("1.2", "1.10"))
print(Solution().compareVersion("1.01", "1.001"))
print(Solution().compareVersion("1.0", "1.0.0.0"))