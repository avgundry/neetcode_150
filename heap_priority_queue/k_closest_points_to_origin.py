import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """One-liner"""
        return heapq.nsmallest(k, points, key=self.dist)
        
        """Optimal method"""
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-self.dist(points[i]), i))

        for j in range(k, len(points)):
            heapq.heappushpop(heap, (-self.dist(points[j]), j))

        return [points[x[1]] for x in heap]


        """Balanced method"""
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-self.dist(points[i]), points[i]))

        for j in range(k, len(points)):
            heapq.heappushpop(heap, (-self.dist(points[j]), points[j]))

        return [x[1] for x in heap]

    def dist(self, points):
        return (points[0]**2 + points[1]**2)**(1/2)
        
        