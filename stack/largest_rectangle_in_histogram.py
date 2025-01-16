from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Hmmm.
        # Begin by transforming into an m x n bit array.
        m = max(heights)
        n = len(heights)
        print(heights[0])
        box = []
        for i in range(m):
            row = [(1 if heights[j] >= i + 1 else 0) for j in range(n)]
            box.append(row)
        for row in box:
            print(row)

        # Best rect found so far. Clearly must be at least the m x 1 rectangle.
        best = m
        def rectArea(i, j, up, right):
            if i + up >= m or j + right >= n or box[i + up][j + right] != 1:
                return -1
            #     return (up - 1) * right
            # elif right >= n or :
            #     return -1
            #     return up * (right - 1)
            else:
                upArea = rectArea(i, j, up + 1, right)
                if upArea == -1:
                    upArea = up * right

                rightArea = rectArea(i, j, up, right + 1)
                if rightArea == -1:
                    rightArea = up * right

                return max(upArea, rightArea)


        # Brute force: examine each valid rectangle, find the maximum.
        for i in range(m):
            for j in range(n):
                # Try two approaches: going up by one, going to the right by one, from each i,j.
                # May be mutually exclusive so...hmmm.
                best = max(best, rectArea(i, j, 0, 0))

        return best



if __name__ == "__main__":
    rects1 = [2,1,5,6,2,3]
    s = Solution()
    print(s.largestRectangleArea(rects1))

        
