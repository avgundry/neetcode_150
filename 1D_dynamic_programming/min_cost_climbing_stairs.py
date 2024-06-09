from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Bottom-up approach"""
        # dp[i] = minimum cost to get *past* step i.
        # So we seek dp[-1]...
        n = len(cost)
        dp = [0 for i in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-2], dp[-1])

        """Top-down approach"""
    #     n = len(cost)
    #     if n == 2:
    #         return min(cost[0], cost[1])
    #     dp = [-1 for i in range(n)]
    #     self.help2(cost, dp, n - 1)
    #     return min(dp[-2], dp[-1])

    # def help2(self, cost, dp, index):
    #     if index < 0 or index > len(cost):
    #         return 0
    #     elif dp[index] != -1:
    #         return dp[index]
        
    #     dp[index] = cost[index] + min(self.help2(cost, dp, index - 1), self.help2(cost, dp, index - 2))
    #     return dp[index]
