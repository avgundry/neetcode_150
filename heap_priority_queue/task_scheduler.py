import heapq
import collections
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        intervals = 0
        heap = []
        count = collections.Counter(tasks)
        # print(count)
        for key, cnt in count.items():
            heapq.heappush(heap, [0, -cnt, key])

        while heap:
            # add cooldown time of next item if there is one
            if heap[0][0] > 0:
                x = heap[0][0]
                intervals += x
                for i in heap:
                    i[0] -= x
                # print(f"heap after reducing interval: {heap}")
                # print(f"intervals after reduction: {intervals}\n")

            # pop it and update what's left
            cooldown, count, key = heapq.heappop(heap)
            for i in heap:
                if i[2] != key:
                    i[0] -= 1
            intervals += 1
            if count < -1:
                heapq.heappush(heap, [cooldown + n, count + 1, key])
            # print(f"intervals: {intervals}")
            # print(f"heap now: {heap}\n\n")

        return intervals
        


if __name__ == "__main__":
    s = Solution()
    s.leastInterval(["A", "A", "B"], 2)

        