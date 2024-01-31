from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Maybe...combine every check into one, using a hashmap?
        # O(n) since checking each position once

        # sets[i] = ith [row, column, grid] set.
        # rows and columns go top to bottom, left to right;
        # grids are numbered left to right, top to bottom, 0-8
        sets = [[set() for _ in range(3)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    continue
                rownum = i
                colnum = j
                # there is a way to do this with math that I'm too
                # tired to think of right now
                if i < 3:
                    if j < 3:
                        gridnum = 0
                    elif j < 6:
                        gridnum = 1
                    else:
                        gridnum = 2
                elif i < 6:
                    if j < 3:
                        gridnum = 3
                    elif j < 6:
                        gridnum = 4
                    else:
                        gridnum = 5
                else:
                    if j < 3:
                        gridnum = 6
                    elif j < 6:
                        gridnum = 7
                    else:
                        gridnum = 8
                
                # gridnum = (i // 3) + (j // 3) # hmm. I think this is it?
                if num in sets[rownum][0] or num in sets[colnum][1] \
                    or num in sets[gridnum][2]:
                    return False
                sets[rownum][0].add(num)
                sets[colnum][1].add(num)
                sets[gridnum][2].add(num)

        return True
                
if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                           ["6",".",".","1","9","5",".",".","."],
                           [".","9","8",".",".",".",".","6","."],
                           ["8",".",".",".","6",".",".",".","3"],
                           ["4",".",".","8",".","3",".",".","1"],
                           ["7",".",".",".","2",".",".",".","6"],
                           [".","6",".",".",".",".","2","8","."],
                           [".",".",".","4","1","9",".",".","5"],
                           [".",".",".",".","8",".",".","7","9"]]))




        
