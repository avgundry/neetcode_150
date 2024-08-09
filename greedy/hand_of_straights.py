import collections
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        # If it's not evenly divisible by the groupsize, we obviously can't rearrange it.
        if n % groupSize != 0:
            return False

        """Dictionary approach."""
        cards = collections.defaultdict(lambda: 0)
        for card in hand:
            cards[card] += 1
        
        smallest = sorted(list(set(hand)), key=lambda x: -x)

        while cards:
            curr = smallest[-1]
            for i in range(curr, curr + groupSize):
                if cards[i] == 0:
                    return False
                else:
                    cards[i] -= 1
                    if cards[i] == 0:
                        del cards[i]
                        smallest.pop()

        return True



        """Brute force"""
        # Greedily remove groups.
        while cards:
            curr = max(cards.elements())
            cards[curr] -= 1
            temp = [curr]
            for _ in range(-2, -1 - groupSize, -1):
                if cards.get(curr - 1):
                    curr -= 1
                    temp.append(curr)
                    cards[curr] -= 1
                    cards = +cards
                else:
                    return False
            cards = +cards


        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
    print(s.isNStraightHand([1,2,3,4,5], 4))