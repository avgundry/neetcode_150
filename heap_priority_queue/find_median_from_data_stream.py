import heapq

class MedianFinder:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.m, self.n = 0, 0
        

    def addNum(self, num: int) -> None:
        # First, place this number in the correct heap.
        if self.m == 0:
            self.maxheap.append(-num)
            self.m += 1
            return
        if num <= -self.maxheap[0]:
            # place in the smaller half of numbers
            heapq.heappush(self.maxheap, -num)
            self.m += 1
        else:
            heapq.heappush(self.minheap, num)
            self.n += 1

        # Then make sure we maintain the property that the maxheap is never smaller
        # than the minheap and is no more than 1 bigger
        if self.m < self.n:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            self.m += 1
            self.n -= 1
        elif self.n + 1 < self.m:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            self.n += 1
            self.m -= 1


    def findMedian(self) -> float:
        if self.m == self.n:
            # Even number of elements so return the average
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == "__main__":
    M = MedianFinder()
    M.addNum(1)
    M.addNum(2)
    print(M.findMedian())
    M.addNum(3)
    print(M.findMedian())

    obj = MedianFinder()
