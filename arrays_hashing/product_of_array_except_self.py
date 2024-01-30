from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #...how? lol
        # Oooh I see. -30 <= nums[i] <= 30.
        # So...yeah.
        bucket = [0 for _ in range(62)]
        for num in nums:
            bucket[num + 30] += 1

        print(bucket)


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    
