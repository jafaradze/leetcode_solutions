class Solution:
    def reverseBits(self, n: int) -> int:
        binN = bin(n)[2:]
        binN = '0' * (32 - len(binN)) + binN
        return int(binN[::-1], 2)