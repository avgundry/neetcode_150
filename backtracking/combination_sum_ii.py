from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort to prevent duplicates when adding to result.
        candidates.sort()

        def backtrack(i, subset, target):
            if target < 0:
                return
            elif i == len(candidates):
                res.append(subset)
                return

            # add subsets containing i
            subset.add(candidates[i])
            backtrack(i + 1, subset, target - candidates[i])
            subset.pop()

            # add subsets *not* containing i
            backtrack(i + 1, subset, target - candidates[i])

        backtrack(0, [], target)

        return res

            