import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort each str in the list...?
        # That's O(n(klogk)) time, where k is the longest length str 
        # in strs?
        # Then group them together...?
        words = collections.defaultdict(list)
        for s in strs:
            words[''.join(sorted(s))].append(s)

        return list(words.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


