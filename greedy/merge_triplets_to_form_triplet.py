from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Iterate through until finding a triplet that has all elements <= target.
        curr = None
        for triplet in triplets:
            if all([triplet[i] <= target[i] for i in range(3)]):
                curr = triplet
                break

        if curr is None:
            return False

        for triplet in triplets:
            if all([triplet[i] <= target[i] for i in range(3)]):
                for i in range(3):
                    curr[i] = max(triplet[i], curr[i])
            if curr == target:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2, 7, 5]))
    print(s.mergeTriplets([[3,5,1],[10,5,7]], [3, 5, 7]))