import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """Heap method."""
        heap = []
        


        """
        Begin with the brute force method of just looping over.
        TLE, as expected. Runs in O(mn) time.
        """
        ret = []
        for query in queries:
            # Curr size of the smallest interval found so far.
            curr = float('inf')
            for inter in intervals:
                if query >= inter[0] and query <= inter[1]:
                    curr = min(curr, inter[1] - inter[0] + 1)
            ret.append(curr)
        
        for i in range(len(ret)):
            if ret[i] == float('inf'):
                ret[i] = -1
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))