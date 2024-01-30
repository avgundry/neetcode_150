from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 2:
            return [nums[1], nums[0]]

        ret = [1 for _ in range(n)]

        ret[1] = nums[0]
        # technically constant space? or...no. hm.
        for i in range(2, n):
            ret[i] = ret[i - 1] * nums[i - 1]

        post = 1
        for i in range(n - 1, -1, -1):
            ret[i] *= post
            post *= nums[i]

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    
