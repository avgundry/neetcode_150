from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Brute force looping"""
        pref_left = nums[::]
        pref_right = nums[::]
        


        # On the first pass, we set up pref_left so that
        # pref_left[i] is the product of all numbers to the left of nums[i].
        for i in range(len(nums)):
            if i == 0:
                pref_left[i] = 1
            else:
                pref_left[i] = nums[i - 1] * pref_left[i - 1]
        
        # On the second pass we set up pref_right so that pref_right[i] is the
        # product of all numbers to the right of nums[i].
        for i in range(len(nums)):
            if i != 0:
                pref_right[-(i + 1)] = nums[-i] * pref_right[-i]
            else:
                pref_right[-(i + 1)] = 1
        
        # Finally, loop over those and multiply each together to get the final answer.
        pref_final = nums[::]
        for i in range(len(nums)):
            pref_final[i] = pref_left[i] * pref_right[i]
 

        return pref_final


        """Unfinished cleaner approach"""
        pref = nums[::]


        # Simultaneously go from left to right, meet in the middle
        # the middle number wil be the product of left and right if even
        # else the middle left number is prod of all #s to left
        # middle right number is prod of all #s to right of it
        # then you can go from there, maybe? 

        # Still need to do two loops.
        # for i in range(len(nums) // 2):
        #     if i == 0:
        #         pref[i] = 1
        #         pref[-(i + 1)] = 1
        #     else:
        #         pref[i] = nums[i - 1] * pref[i - 1]
        #         pref[-(i + 1)] = nums[-i] * pref[-i]

        # pref[i + 1] = nums[i] * pref[i] * nums[i + 2] * pref[i + 2]
        # Now loop to 'combine' the two sides, starting from the middle.
        for i in range(len(nums) // 2, -1):
            pref[i] *= pref[i ]

        
if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    
