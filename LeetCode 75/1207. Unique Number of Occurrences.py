from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = d.get(arr[i], 0) + 1
        val = d.values()
        return len(val) == len(set(val))