from collections import Counter, deque
from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Deque solution"""
        currmax = float('-inf')
        dq = deque()
        ret = []

        for i in range(k):
            currmax = max(currmax, nums[i])
            dq.append(nums[i])

        ret.append(currmax)


        for i in range(k, len(nums)):
            if dq.popleft() == currmax:
                currmax = max(dq, default=float('-inf'))
            currmax = max(currmax, nums[i])
            dq.append(nums[i])
            ret.append(currmax)

        return ret




        """Brute force solution: iterate over each window"""
        n = len(nums)
        out = []

        for i in range(n - k + 1):
            window = nums[i:i + k]
            out.append(max(window))

        return out

        

if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,-1], 1))
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


        