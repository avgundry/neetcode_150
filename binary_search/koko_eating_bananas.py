import math 
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            curr = self.timeToEat(piles, mid)
            if curr <= h:
                right = mid
            else:
                left = mid + 1
                
        return left

    def timeToEat(self, piles, k):
        return sum(math.ceil(pile / k) for pile in piles)
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)

        return total


                
if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], 8))
    print(s.minEatingSpeed([30,11,23,4,20], 5))