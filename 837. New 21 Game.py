from functools import lru_cache

class Solution:
    def new21Game(self, N: int, K: int, maxPoints: int) -> float:
        @lru_cache(None)
        def dfs(current_points: int) -> float:
            if current_points >= K:
                return float(current_points <= N)
            if current_points == K - 1:
                return min(N - K + 1, maxPoints) / maxPoints
            return dfs(current_points + 1) + (dfs(current_points + 1) - dfs(current_points + maxPoints + 1)) / maxPoints
        return dfs(0)