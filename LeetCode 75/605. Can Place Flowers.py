from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed == []:
            return n == 0
        elif len(flowerbed) == 1:
            return flowerbed == [0] and n <= 1 or flowerbed == [1] and n == 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1:i + 2] == [0, 0, 0]:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
            
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-2] = 1
            n -= 1
        
        return n <= 0

print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
print(Solution().canPlaceFlowers([1,0,0,0,1], 2))

print(Solution().canPlaceFlowers([], 0))
print(Solution().canPlaceFlowers([], 1))
print(Solution().canPlaceFlowers([0], 1))
print(Solution().canPlaceFlowers([0], 0))
print(Solution().canPlaceFlowers([0], 2))
