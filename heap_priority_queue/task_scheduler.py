import heapq
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """priority queue"""
        count = Counter(tasks)
        q = []
        time = 0
        while count:
            time += 1
            count.most_common(1)[0]



if __name__ == "__main__":
    s = Solution()
    s.leastInterval(["A", "A", "B"], 2)

        