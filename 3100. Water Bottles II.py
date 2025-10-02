class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        bottlesDrunk = 0
        while numBottles != 0 or emptyBottles >= numExchange:
            if numBottles != 0:
                bottlesDrunk += numBottles
                emptyBottles += numBottles
                numBottles = 0
                continue
            else:
                emptyBottles -= numExchange
                numBottles += 1
                numExchange += 1
        return bottlesDrunk
    
