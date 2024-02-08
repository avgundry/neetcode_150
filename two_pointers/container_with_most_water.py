from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Oh I misread. Sigh. Well at least this becomes
        # way easier this way.
        n = len(height)
        if n == 2:
            return min(height)

        """Two pointer solution."""

        # Have two pointers.
        left = 0
        right = n - 1

        # Store the current volume for convenience.
        curr = min(height[left], height[right]) * (right - left)
        # Store the best we've found so far.
        best = curr

        # Technically O(n) time, but definitely suboptimal otherwise.
        while left < right:
            # If moving left forward increases container size, do so.
            if min(height[left + 1], height[right]) * (right - left - 1) >= curr:
                left += 1
                best = max(best, min(height[left + 1], height[right]) * (right - left))
            # Otherwise, if moving right backwards increases container size, do so.
            elif min(height[left], height[right - 1]) * (right - left - 1) >= curr:
                right -= 1
                best = max(best, min(height[left], height[right - 1]) * (right - left))
            # If neither of those cases apply, move both towards the center...?
            # Hmmm...
            # Maybe ONLY move the pointer that points to the smaller one.
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
            curr = min(height[left], height[right]) * (right - left)

        return best
        

        """Brute force solution."""
        # Simply go over each index, find the best matching container for that index.
        # To begin with ultra inefficiency we store in an array.
        best_heights = [-1] * n
        for i in range(n):
            for j in range(i, n):
                best_heights[i] = max(best_heights[i],  \
                        (j - i) * min(height[i], height[j]))

        return max(best_heights)

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea([1,8,100,2,100,4,8,3,7]))

        