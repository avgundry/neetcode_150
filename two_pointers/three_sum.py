from collections import defaultdict
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # split into positives, negatives, zeroes
        positives = dict()
        negatives = dict()
        zeroes = 0

        for i in range(len(nums)):
            if nums[i] < 0:
                negatives[nums[i]] = negatives.get(nums[i], 0) + 1
            elif nums[i] > 0:
                positives[nums[i]] = positives.get(nums[i], 0) + 1
            else:
                zeroes += 1

        triplets = []
        # Begin with case of all zeroes
        if zeroes >= 3:
            triplets.append([0, 0, 0])

        if zeroes:
            for pos in positives:
                if negatives.get(-pos):
                    triplets.append([0, pos, -pos])
        
        # Then all the cases *not* involving 0.
        for pos in positives.keys():
            # Two positives
            for pos2 in positives.keys():
                if (positives[pos] > 1 or pos != pos2) and negatives.get(-pos2 - pos) \
                and sorted([pos, pos2, -pos - pos2]) not in triplets:
                    triplets.append([pos, pos2, -pos2 - pos])

        # Two negatives
        for neg in negatives.keys():
            for neg2 in negatives.keys():
                if (negatives[neg] > 1 or neg != neg2) and positives.get(-neg2 - neg) \
                and sorted([neg, neg2, -neg2 - neg]) not in triplets:
                    triplets.append(sorted([neg, neg2, -neg2 - neg]))

        return triplets

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))

        