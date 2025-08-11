from math import prod

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        binN = bin(n)[2:]
        powers = []
        for i, p in enumerate(binN[::-1]):
            if p == '1':
                powers.append(1 << i)
        res = []
        for query in queries:
            l, r = query
            res.append((prod(powers[l:r + 1])) % (10 ** 9 + 7))
        return res