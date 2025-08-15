class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        binN = bin(n)[2:]
        return binN.count('1') == 1 and binN.count('0') % 2 == 0 and n > 0