class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        i = 0
        while i <= 30:
            if sorted(str(n)) == sorted(str(1 << i)):
                return True
            i += 1
        return False