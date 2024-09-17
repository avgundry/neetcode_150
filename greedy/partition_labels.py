from collections import Counter
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Dictionary method.
        """
        # Counter of elements in s[left:right].
        right_count = Counter(s)
        seen = set()
        ret = []
        # print(right_count)
        left = -1 
        for right in range(len(s)):
            seen.add(s[right])
            right_count[s[right]] -= 1
            right_count = +right_count
            if right_count[s[right]] == 0 and seen.isdisjoint(set(right_count.keys())):
                ret.append(right - left)
                left = right
        return ret

        """
        Brute force set iteration over each index point.
        O(n^2) time.
        """
        ret = []
        left = 0
        for right in range(len(s)):
            if set(s[left:right]).isdisjoint(set(s[right:])) and right - left != 0:
                ret.append(right - left)
                left = right

        ret.append(len(s) - sum(ret))


        return ret



if __name__ == "__main__":
    s = Solution()
    # print(s.partitionLabels("ababcbacadefegdehijhklij"))
    print(s.partitionLabels("aabb"))
    print(s.partitionLabels("aaba"))
    print(s.partitionLabels("abccbcc"))
    print(s.partitionLabels(""))
    # print(s.partitionLabels("abab"))
        