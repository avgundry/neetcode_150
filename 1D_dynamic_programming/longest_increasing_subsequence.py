from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        # Hmm. Let dp[i] be the LIS ending in nums[i].
        dp = [0 for _ in range(n)]

        dp[0] = 1
        for i in range(n):
            temp = [dp[j] for j in range(i) if nums[j] < nums[i]]
            dp[i] = max(temp, default=0) + 1
            # dp[i] = max([dp[j] for j in range(i) if nums[j] < nums[i]], default=0) + 1

        return max(dp)
       
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))