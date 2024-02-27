from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[(mid - 1) % n] < nums[mid] and nums[mid] > nums[(mid + 1) % n]:
                # Found the end of the original array.
                left = right + 1
            elif nums[left] > nums[mid]:
                # must be in the left half, since at some point in left
                # half it must switch from increasing to decreasing.
                right = mid - 1
            else:
                left = mid + 1

        # We know the start is the smallest since it's in sorted order,
        # so just return that.
        return nums[(mid + 1) % n]
        
if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
    print(s.findMin([4,5,6,7,0,1,2]))
    print(s.findMin([11,13,15,17]))