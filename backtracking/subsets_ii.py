from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subs = [[]]

        for num in nums:
            n = len(subs)
            for i in range(n):
                temp = subs[i] + [num]
                if temp not in subs:
                    subs.append(temp)

        return subs
        