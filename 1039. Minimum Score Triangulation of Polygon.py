from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        n = len(values)
        m = n

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for length in range(3,m+1):
            for i in range(n-length+1):
                j = i+length - 1
                dp[i][j] = float('inf')
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j], values[i]*values[k]*values[j]+dp[i][k]+dp[k][j])

        return dp[0][n-1]