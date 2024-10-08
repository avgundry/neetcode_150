from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """Two-pointer approach, O(n) time and O(1) space"""
        n = len(nums)
        if n <= 2:
            return max(nums)
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            temp = prev
            prev = curr
            curr = max(temp + nums[i], curr)


        return curr

        """Bottom-up dp approach, O(n) time and space"""
        # Let dp[i] represent the maximum amount of money obtainable by robbing
        # houses up to house[i].
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))
        