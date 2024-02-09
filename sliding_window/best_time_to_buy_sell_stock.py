from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Sliding window method"""
        n = len(prices)
        left = right = 0
        best = 0
        while right < n - 1:
            if prices[right] < prices[left]:
                left = right
            right += 1
            best = max(best, prices[right] - prices[left])
        
        return best

        """Brute force method"""
        best = 0
        n = len(prices)
        for i in range(n):
            for j in range(i, n):
                best = max(best, prices[j] - prices[i])

        return best
        # sliding window method.

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([2,1,2,1,0,1,2]))