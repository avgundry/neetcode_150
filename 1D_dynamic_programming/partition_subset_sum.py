from collections import defaultdict
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Optimal dp approach"""
        s = sum(nums)
        # If the sum of all numbers is not even, we can't split it evenly
        # since each num is an int.
        if s % 2 != 0:
            return False

        # dp[i] represents that summing to i is possible given the array of nums.
        dp = [True] + [False] * int(s / 2)
        for num in nums:
            for j in range(len(dp) - 1, num - 1, -1):
                dp[j] = dp[j - num] or dp[j]
        
        return dp[int(s / 2)]

        s = sum(nums)
        n = len(nums)
        # If the sum of all numbers is not even, we can't split it evenly
        # since each num is an int.
        if s % 2 != 0:
            return False

        # dp[i] represents that summing to i is possible given the array of nums.
        dp = [True] + [False] * int(s / 2)
        for num in nums:
            for j in range(len(dp) - 1, -1, -1):
                # print(j)
                if j - num < 0:
                    dp[j] = False or dp[j]
                else:
                    dp[j] = (True and dp[j - num]) or dp[j]
        
        return dp[int(s / 2)]
       

if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1,5,11,5]))
    print(s.canPartition([1,2,3,5]))
    print(s.canPartition([1,2,5]))
    print(s.canPartition([2, 2, 1, 1]))




