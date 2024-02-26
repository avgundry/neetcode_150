from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Can optimize by combining the two loops below,
        # but for now separate them.
        n = len(nums)

        # First, find where the array was rotated to.
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[(mid - 1) % n] and nums[mid] < nums[(mid + 1) % n]:
                # This is in sorted order.
                # god idk. I don't have time to write this out today :\

    def binSearch(self, nums):
        