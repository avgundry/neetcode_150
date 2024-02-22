from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Ugh. Start over.
        # We need to binary search for what row, exactly?
        # The first row such that:
        # matrix[row][0] <= target AND matrix[row + 1][0] > target.
        # Does that cover all cases?
        # Or, if row + 1 out of bounds, then just find the row such that
        # matrix[row][0] <= target.
        # If that doesn't exist we return false.
        n = len(matrix)
        top = 0
        bottom = n - 1
        row = None

        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] <= target:
                if row + 1 == n or matrix[row + 1][0] > target:
                    # Then target MUST be in our current row *if* it
                    # exists.
                    top = bottom + 1
                else:
                    # Otherwise we still need to increment.
                    top = row + 1
            else:
                bottom = row - 1

        # If we didn't find a row it could be in, it doesn't exist.
        if row == None:
            return False
        
        # Binary search the row.
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return matrix[row][mid] == target
            
                    

        

if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
    print(s.searchMatrix([[1],[3]], 3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30))
    print(s.searchMatrix([[-8,-8,-7,-7,-6,-5,-3,-2],[0,0,1,3,4,6,8,8],[11,12,14,16,18,18,19,19],[22,23,25,27,28,30,30,31],[34,35,37,39,40,42,43,45],[48,50,51,51,53,54,55,57],[58,60,62,62,62,63,63,65],[68,69,71,72,72,72,74,76]], 76))
            

        