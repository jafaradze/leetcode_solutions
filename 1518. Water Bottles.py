class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        while True:
            res += numBottles
            empty += numBottles % numExchange
            numBottles //= numExchange
            numBottles += empty // numExchange
            empty %= numExchange
            if empty < numExchange and numBottles == 0:
                break
        return res