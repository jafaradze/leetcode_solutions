from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * len(energy)
        for i in range(len(energy) - 1, -1, -1):
            if i + k < len(energy):
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
        return max(dp)

Solution().maximumEnergy(energy = [5,2,-10,-5,1], k = 3)