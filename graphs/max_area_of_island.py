from typing import List

from collections import defaultdict

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Approach with mutating grid"""
        max_area = 0

        m = len(grid)
        n = len(grid[0])

        def explore_island(i, j):
            """
            Explores an island to find its area and mark all of it as visited.
            """
            # If out of bounds, simply return.
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                return 1 + explore_island(i + 1, j) + explore_island(i - 1, j) \
                        + explore_island(i, j + 1) + explore_island(i, j - 1)


        # This *could* be sped up and made cleaner at the cost of modifying the grid,
        # by setting each value of the grid to 0 after visiting it.
        for i in range(m):
            for j in range(n):
                if not (grid[i][j] == 0):
                    # Only occurs when hitting a new island, in which we update our max area.
                    max_area = max(explore_island(i, j), max_area)

        return max_area
        """Approach without mutating grid"""
        # visited[i][j] being 1 means we have already visited [i][j]
        visited = defaultdict(dict)
        max_area = 0

        m = len(grid)
        n = len(grid[0])

        def explore_island(i, j):
            """
            Explores an island to find its area and mark all of it as visited.
            """
            # If out of bounds, simply return.
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited.get(i, {}).get(j) == 1:
                return 0
            else:
                visited[i][j] = 1
                return 1 + explore_island(i + 1, j) + explore_island(i - 1, j) \
                        + explore_island(i, j + 1) + explore_island(i, j - 1)


        # This *could* be sped up and made cleaner at the cost of modifying the grid,
        # by setting each value of the grid to 0 after visiting it.
        for i in range(m):
            for j in range(n):
                if not(grid[i][j] == 0 or (visited.get(i) and visited[i].get(j))):
                    # Only occurs when hitting a new island, in which we update our max area.
                    max_area = max(explore_island(i, j), max_area)

        return max_area
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                             [0,0,0,0,0,0,0,1,1,1,0,0,0],
                             [0,1,1,0,1,0,0,0,0,0,0,0,0],
                             [0,1,0,0,1,1,0,0,1,0,1,0,0],
                             [0,1,0,0,1,1,0,0,1,1,1,0,0],
                             [0,0,0,0,0,0,0,0,0,0,1,0,0],
                             [0,0,0,0,0,0,0,1,1,1,0,0,0],
                             [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
        