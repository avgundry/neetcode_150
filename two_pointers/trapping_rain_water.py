from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        curr = 0
        total = 0
        n = len(height)

        for i in range(1, n):
            if height[i] >= height[left]:
                total += curr
                curr = 0
                left = i
            else:
                curr += height[left] - height[i]

        # then sweep backwards if we didn't capture everything.
        if left != n - 1:
            curr = 0
            right = n - 1
            for i in range(n - 1, left - 1, -1):
                if height[i] >= height[right]:
                    total += curr
                    curr = 0
                    right = i
                else:
                    curr += height[right] - height[i]

        return total


        