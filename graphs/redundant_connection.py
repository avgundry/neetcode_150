from collections import defaultdict, deque
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # I suppose...
        # starting from node 1, BFS until we find a node that's already been explored
        # then we can remove the connection that took us there?
        edges = deque(edges)
        seen = set()
        while edges:
            curr = edges.popleft()
            if curr[0] in seen and curr[1] in seen:
                return curr
            seen.add(curr[0])
            seen.add(curr[1])
            

        
        

if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection([[1,2],[1,3],[2,3]]))