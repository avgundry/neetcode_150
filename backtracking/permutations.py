import collections
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = collections.deque()
        self.helper(nums, ret, [])
        return ret

    def helper(self, nums, ret, curr):
        if not nums:
            ret.append(curr)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i + 1:], ret, curr + [nums[i]])
            




if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))