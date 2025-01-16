from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = dict()
        # Let lengths[i] = the longest sequence containing i.
        # So if we have nums = 1,2,3, 5, then
        # lengths[1] = lengths[2] = lengths[3] = (1, 3)
        # and lengths[5] = (5, 5)

        for num in nums:
            x = lengths.get(num - 1)
            y = lengths.get(num + 1)
            if x and y:
                # union the two
                newseq = (min(x[0], y[0]), max(x[1], y[1]))
                for i in range(newseq[0], newseq[1] + 1):
                    lengths[i] = newseq
            elif x and num > x[1]:
                newseq = (x[0], num)
                for i in range(x[0], num + 1):
                    lengths[i] = newseq
            elif y and num < y[0]:
                for i in range(num, y[1] + 1):
                    lengths[i] = (num, y[1])
            else:
                lengths[num] = (num, num)

        return len(max(set(lengths.values()), key=lambda x: x[1] - x[0] + 1))
            

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))
    print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(s.longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]))
    print(s.longestConsecutive([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]))