import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        # Cannot eat this quickly.
        if n > h:
            return -1
        # In this case we know we must eat one pile every hour.
        elif n == h:
            return max(piles)

        # Ok. We know it's binary search, so let's just try brute forcing
        # the solution within that context: binary search values of k, checking
        # if each of them are valid.
        # First, find the range in which we know she can eat in that time.
        # We know the upper bound is eating max(piles) each hour, as then 
        # she'll finish one pile per hour.
        right = max(piles)
        # So we need to know the lower bound...
        # Simply start it at 0?
        left = 1
        # Then binary search.
        while left < right:
            mid = (left + right) // 2
            tte = self.timeToEat(piles, mid)
            if tte == h and self.timeToEat(piles, mid - 1) > h:
                return mid
            if tte <= h:
                right = mid
            else:
                # Here we are eating too slow so must increase left bound.
                left = mid + 1

        return (left + right) // 2

    def timeToEat(self, piles, k):
        """
        Returns the time to eat piles at k bananas per hour.
        """
        # Time to eat all the piles when eating k per hour.
        total = 0

        for pile in piles:
            total += math.ceil(pile / k)

        return total

 
if __name__ == "__main__":
    s = Solution()
    # print(s.minEatingSpeed([3,6,7,11], 8))
    # print(s.minEatingSpeed([30,11,23,4,20], 5))
    print(s.minEatingSpeed([30,11,23,4,20], 6))