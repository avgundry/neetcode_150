from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Hmm. Definitely a dp problem...
        # Consider the case with 1 balloons. Obviously, we want to just pop it...
        # For the case with 2 balloons it doesn't matter what balloon we pop...no it DOES
        # AB we either have AB + B or AB + A
        # With 3 balloons, A, B, C, we get:
        # AB + BC + B
        # AB + BC + C
        # ABC + AC + C
        # ABC + AC + A
        # BC + AC + A
        # BC + AC + C
        # This comes out to...what. ABC + coins(AC), AB + coins(BC), BC + coins(AC). Interesting.

        # With 4 balloons... ABCD...hmmm
        # We basically maximize from the following options:
        # AB + coins(BCD), ABC + coins(ACD), BCD + coins(ABD), CD + coins(ABC)
        # Then...yeah, how else would we DFS it...? Hm.
        # I don't see how it would be 2D; if anything maybe it's something like n-d lol.
        # Do something crazy like make each index be a 1 if included or 0 if not and use bitstrings
        # as the keys...or just use a regular hashmap.

        # So in this case...just let dp[tuple] = maxCoins(tuple).
        dp = dict()
        def balloonValue(arr, i):
            left = 1
            right = 1
            if i - 1 >= 0:
                left = arr[i - 1]
            if i + 1 < len(arr):
                right = arr[i + 1]
            return left * arr[i] * right

        # def max2(tup, i):
        #     return balloonValue(tup, i) + dfs_dp(tup[:i] + tup[i + 1:])
        def dfs_dp(tup):
            if len(tup) == 0:
                return 0
            dp[tup] = dp.get(tup, max([balloonValue(tup, i) + dfs_dp(tup[:i] + tup[i + 1:]) for i in range(len(tup))]))
            # if dp.get(tup, False):
            #     return dp[tup]
            # out = []
            # for i in range(len(tup)):
            #     out.append(balloonValue(tup, i) + dfs_dp(tup[:i] + tup[i + 1:]))
            # dp[tup] = max(out)
            return dp[tup]

        return dfs_dp(tuple(nums))
        # return dfs(nums)

if __name__ == "__main__":
    import cProfile, pstats
    # profiler = cProfile.Profile()
    # profiler.enable()
    s = Solution()
    print(s.maxCoins([3,1,5,8]))
    print(s.maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2,9]))
    # profiler.disable()
    # profiler.dump_stats('profile_data.prof')

    # stats = pstats.Stats('profile_data.prof')
    # stats.sort_stats('cumtime')  # Sort by cumulative time
    # stats.print_stats()



        