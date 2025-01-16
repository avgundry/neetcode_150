from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow = 0
        fast = nums[0] % n

        while slow != fast:
            # Find the cycle.
            slow = (nums[slow] + slow) % n
            fast = (nums[fast] + fast) % n
            fast = (nums[fast] + fast) % n

        # Found the cycle. Restart fast at the beginning. Why does this work?
        fast = 0
        while slow != fast:
            slow = (nums[slow] + slow) % n
            # fast = (nums[fast] + fast) % n
            fast = (nums[fast] + fast) % n

        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1,3,4,2,2]))
    print(s.findDuplicate([3,1,3,4,2]))
       