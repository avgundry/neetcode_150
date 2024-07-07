from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """suboptimal DP method"""
        # dict where key is amount, val is fewest # of coins to make that amount.
        dp = dict()
        dp[0] = 0
        for coin in coins:
            dp[coin] = 1

        return self.dpHelper(coins, amount, dp)
    
    def dpHelper(self, coins, amount, dp):
        if dp.get(amount):
            return dp[amount]
        elif amount < 0:
            return -1
        elif amount == 0:
            return 0
        else:
            temp = []
            for coin in coins:
                x = self.dpHelper(coins, amount - coin, dp)
                if x >= 0:
                    temp.append(x)
            dp[amount] = min(temp, default=-2) + 1
            return dp[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([2], 3))

