from collections import Counter, deque
from typing import List
import heapq


class Solution:
    class Deque:
        def __init__(self) -> None:
            self.dq = deque()
            self.best = None
        
        def add_num(self, num):
            self.dq.append(num, 0)????

        
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Two pointers"""
        # Oh. Maybe simplest is easiest.
        biggest = float('-inf')
        left = right = 0
        while right < k:
            biggest = max(biggest, nums[right])
            right += 1

        
        """Hashmap solution"""
        # I believe slightly better is to use a heap and dictionary in
        # conjunction with one another. We can lazily delete from the
        # heap in that case

        # Used to quickly find the biggest element.
        heap = []
        # All numbers and their counts in the list
        counts = Counter()
        n = len(nums)
        ret = []

        for i in range(n):
            heapq.heappush(heap, -nums[i])
            counts[nums[i]] += 1
            if i < k - 1:
                continue
            else:
                while counts.total() > k: 
                    counts[nums[i - k]] -= 1
                # checks in O(1) time
                while (-heap[0]) not in (+counts):
                    # Pops in O(k) time.
                    counts[-heap[0]] -= 1
                    heapq.heappop(heap)
                ret.append(-heap[0])

        return ret


        # """Brute force solution"""
        # heap = []
        # n = len(nums)
        # ret = []
        # for i in range(n):
        #     heapq.heappush(heap, -nums[i])
        #     if i == k - 1:
        #         ret.append(-heap[0])
        #     if i >= k:
        #         # this is super brute force almost solely because of this:
        #         # remove elements at each step.
        #         # uses linear time, so it becomes O(nk) time
        #         heap.remove(-nums[i - k])
        #         heapq.heapify(heap)
        #         ret.append(-heap[0])

        # return ret

if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,-1], 1))


        