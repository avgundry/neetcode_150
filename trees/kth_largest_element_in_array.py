import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Standard heap solution"""
        heap = []
        for num in nums:
            # print(f"num: {num}")
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
            # print(f"heap after pushing num {num}: \n{heap}\n\n")
        
        return heap[0]

        """One-liner"""
        return heapq.nlargest(k, nums)[-1]