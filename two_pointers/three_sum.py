from collections import defaultdict
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """brute force approach with sorted tuples"""
        # 2sum can be done in...? time.
        # obviously O(n^2); but I think it can be done in O(n) time by hashing each #, yeah.
        # So then 3sum can be done in O(n^2) as well...

        n = len(nums)
    
        # split into positive, negative, zeros
        positives = dict()
        negatives = dict()

        # simply count the number of zeros
        zeroes = 0

        # loop through and add each to the respective dict, counting how many we have
        for i in range(n):
            curr = nums[i]
            if curr < 0:
                negatives[curr] = negatives.get(curr, 0) + 1
            elif curr > 0:
                positives[curr] = positives.get(curr, 0) + 1
            else:
                zeroes += 1

        # where we store the array of triplets
        triplets = set()

        if zeroes >= 3:
            triplets.add((0, 0, 0))

        # if there's at least one zero
            # for each positive number
                # if its negative exists, add that triplet

            # for each negative number
                # if its positive exists, add that triplet
        if zeroes:
            for pos in positives.keys():
                if -pos in negatives.keys():
                    triplets.add(tuple(sorted((pos, -pos, 0))))

        for pos in positives.keys():
            for pos2 in positives.keys():
                if -(pos + pos2) in negatives.keys() and (pos != pos2 or positives[pos] > 1):
                    triplets.add(tuple(sorted((pos, pos2, -(pos + pos2)))))
        for neg in negatives.keys():
            for neg2 in negatives.keys():
                if -(neg + neg2) in positives.keys() and (neg != neg2 or negatives [neg] > 1):
                    triplets.add(tuple(sorted((neg, neg2, -(neg + neg2)))))

        return list(set(triplets))









        # split into positives, negatives, zeroes
        # positives = dict()
        # negatives = dict()
        # zeroes = 0

        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         negatives[nums[i]] = negatives.get(nums[i], 0) + 1
        #     elif nums[i] > 0:
        #         positives[nums[i]] = positives.get(nums[i], 0) + 1
        #     else:
        #         zeroes += 1

        # triplets = []
        # # Begin with case of all zeroes
        # if zeroes >= 3:
        #     triplets.append([0, 0, 0])

        # if zeroes:
        #     for pos in positives:
        #         if negatives.get(-pos):
        #             triplets.append([0, pos, -pos])
        
        # # Then all the cases *not* involving 0.
        # for pos in positives.keys():
        #     # Two positives
        #     for pos2 in positives.keys():
        #         if (positives[pos] > 1 or pos != pos2) and negatives.get(-pos2 - pos) \
        #         and sorted([pos, pos2, -pos - pos2]) not in triplets:
        #             triplets.append([pos, pos2, -pos2 - pos])

        # # Two negatives
        # for neg in negatives.keys():
        #     for neg2 in negatives.keys():
        #         if (negatives[neg] > 1 or neg != neg2) and positives.get(-neg2 - neg) \
        #         and sorted([neg, neg2, -neg2 - neg]) not in triplets:
        #             triplets.append(sorted([neg, neg2, -neg2 - neg]))

        # return triplets

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))

        