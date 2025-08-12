class Solution:
    def numberOfWays(self, total_sum: int, exponent: int) -> int:
        m = 10 ** 9 + 7

        dp = [[0] * (total_sum + 1) for _ in range(total_sum + 1)]
        dp[0][0] = 1
      
        for k in range(1, total_sum + 1):
            power = k ** exponent
            for j in range(total_sum + 1):
                dp[k][j] = dp[k - 1][j]
                if power <= j:
                    dp[k][j] = (dp[k][j] + dp[k - 1][j - power]) % m
        return dp[total_sum][total_sum]