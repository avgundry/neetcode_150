from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = dict()
        # Hm
        # Iterate over each number. Let dict[num] represent the longest
        # length consecutive sequence that contains num.
        # Then as we go through each num, we check if num - 1 or 
        # num + 1 in list.
        # If it is...then increment that by 1? Hm.
        # Maybe, for each key num, store the range of consec elements..?
        # No that's not O(n) time...wow I'm tired.

        


