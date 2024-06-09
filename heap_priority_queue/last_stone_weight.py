import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Turn the list into a maxheap: to do so, we must 
        # negate all the stones' weights.
        stones = [-x for x in stones]
        heapq.heapify(stones)

        """Optimized method."""
        while len(stones) > 1:
            y = heapq.heappop(stones)
            if y != stones[0]:
                heapq.heapreplace(stones, y - stones[0])
            else:
                heapq.heappop(stones)
        
        return -stones[0] if len(stones) > 0 else 0

        """Brute force method."""
        # while len(stones) > 1:
        #     y = heapq.heappop(stones)
        #     x = heapq.heappop(stones)
        #     if x != y:
        #         y -= x
        #         heapq.heappush(stones, y)

        
        # return -stones[0] if len(stones) > 0 else 0