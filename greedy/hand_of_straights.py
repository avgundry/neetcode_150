import collections
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = collections.Counter(sorted(hand))
        while count:
            card = list(count.keys())[0]
            if all([count[card + i] > 0 for i in range(groupSize)]):
                for i in range(groupSize):
                    count[card + i] -= 1
                count = +count
            else:
                return False

        return True



if __name__ == "__main__":
    s = Solution()
    print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
    print(s.isNStraightHand([1,2,3,4,5], 4))
    print(s.isNStraightHand([1], 1))