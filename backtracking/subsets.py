from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Brute force method"""
        subs = [[]]
        for num in nums:
            currlen = len(subs)
            for i in range(currlen):
                subs.append(subs[i] + [num])

        return subs

        

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))