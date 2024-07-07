from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """DP approach"""
        # dict of target: subsets that combine to that target
        # end goal is to return original target
        dp = dict()
        self.dpHelper(candidates, target, dp)

        return dp.get(target, [])

    def dpHelper(self, candidates, target, dp):
        for cand in candidates:
            if cand <= target:
                x = dp.get(cand)
                if x:
                    return x
                else:
                    dp[target - cand] = self.dpHelper()


        """Brute force recursion"""
        res = []
        self.helper(candidates, target, [], res)
        return list(set(res))

    def helper(self, candidates, target, nums, res) -> List[List[int]]:
        if target < 0:
            return
        elif target == 0:
            res.append(sorted(tuple(nums)))
        else:
            for cand in candidates:
                self.helper(candidates, target - cand, nums + [cand], res)

if __name__ == "__main__":
    s = Solution()
        