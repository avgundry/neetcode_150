from collections import defaultdict
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Topological sort method
        """
        # Possible directions to move in at each step.
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(matrix)
        n = len(matrix[0])
        graph = defaultdict(dict)
        for row in range(m):
            for col in range(n):
                increases = []
                curr = matrix[row][col]
                for d in dirs:
                    other_row = row + d[0]
                    other_col = col + d[1]
                    if not (0 <= other_row < m and 0 <= other_col < n):
                        continue
                    other_curr = matrix[other_row][other_col]
                    if other_curr > curr:
                        increases.append((other_row, other_col))
                graph[row][col] = increases

                # graph[row][col] = [(row + dir[0], col + dir[1]) for dir \
                #                    in dirs if 0 < row + dir[0] < m and 0 < col + dir[1] < n \
                #                    and matrix[row][col] < matrix[row + dir[0]][col + dir[1]]]
        
        print(graph)
        def graphlen(key):
            curr = key
        maxes = []
        for key in graph.keys():
            maxes.append(pathlen(key))
        return graph

        """
        Hmm. Backtracking method to begin...?
        """

if __name__ == "__main__":
    mat1 = [[9,9,4],[6,6,8],[2,1,1]]
    s = Solution()
    x = s.longestIncreasingPath(mat1)
    for row in mat1:
        print(row)
    print()
    for row in x.keys():
        for col in x[row].keys():
            print(f"x[{row}][{col}] for mat1[row][col] {mat1[row][col]} = {x[row][col]}")
        # print(row)


        