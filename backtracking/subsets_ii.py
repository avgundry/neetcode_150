from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Backtracking method."""
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                # Append a copy of the completed subset.
                res.append(subset[::])
                return

            # Create all subsets including nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            
            # Create all subsets NOT including nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])

        return res

        """Loop method."""
        nums.sort()
        subs = [[]]

        for num in nums:
            n = len(subs)
            for i in range(n):
                temp = subs[i] + [num]
                if temp not in subs:
                    subs.append(temp)

        return subs
        