from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        # Ok solve house robber i first.
        # This solves standard house robber problem.
        # To extend to case it's circular...
        # Solve dp problem when excluding nums[0]
        # Then solve it when excluding nums[-1] and including nums[0]...
        def solve(arr):
            m = len(arr)
            if m <= 3:
                return max(arr)

            dp = [0 for _ in range(m)]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, m):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[-1]

        no0 = solve(nums[1:])
        with0 = nums[0] + solve(nums[1:-1])

        # ???
        return max(no0, with0)

        n = len(nums)
        if n <= 3:
            return max(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        # dp[-1] = max(dp[0] + dp[-2], dp[-1] + dp[-3])
        # dp[-1] -= nums[0]

        # dp[0] = max(dp[-2] + dp[0], dp[-1])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
