from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """Brute force solution."""
        out = []
        for i in range(n + 1):
            out.append(bin(i).count('1'))

        return out
        
if __name__ == "__main__":
    s = Solution()
    print(s.countBits(17))