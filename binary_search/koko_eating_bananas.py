from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Super brute force because I cannot figure out how this
        relates to binary search?"""
        n = len(piles)

        if n > h:
            # Cannot eat them all in time.
            return False
        if n == h:
            return max(piles)

        # Binary search between ceil(sum(piles) / h ) and max(piles)???
        total = sum(piles)
        left = total // h + 1
        right = max(piles)

        # Maybe could DP and build out a time matrix...hm
        while left <= right:
            mid = (left + right) // 2
            curr = self.verify_pile_time(piles, mid)
            if curr == h:
                # left = right + 1
                break
                # return curr
            elif curr < h:
                # need to eat it slower
                left = mid + 1
            else:
                # need to eat it faster
                right = mid - 1

        mid = (left + right) // 2
        curr = self.verify_pile_time(piles, mid)
        return curr

    def verify_pile_time(self, piles, k):
        time = 0
        for pile in piles:
            time += -(pile // -k)

        return time
        
if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], 8))
    print(s.minEatingSpeed([30,11,23,4,20], 5))