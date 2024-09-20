from collections import Counter, deque
from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < k or k == 0:
            return []
        elif k == 1:
            return nums

        # A heap that lazily stores the current window.
        kheap = []
        # Counter to keep track of how many of each num are in the current window.
        count = Counter()
        # The array we return.
        out = []

        for i in range(n):
            curr = nums[i]
            count[curr] += 1
            heapq.heappush(kheap, -curr)
            if i == k - 1:
                out.append(-kheap[0])
            if i <= k - 1:
                continue
            else:
                prev = nums[i - k]
            
            # Slide the window by decrementing the count.
            count[prev] -= 1
            # Remove any elements in the heap that are no longer in the window.
            while count[-kheap[0]] <= 0:
                heapq.heappop(kheap)

            # Then add the largest element to our output.
            out.append(-kheap[0])

        return out

if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))
    print(s.maxSlidingWindow([7, 2, 4], 2))
    print(s.maxSlidingWindow([1,-1], 1))
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


        