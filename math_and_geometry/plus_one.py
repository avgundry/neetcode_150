from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[-1] == 9:
            return [1, 0]
        if digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]
        else:
            return digits[:-1] + [digits[-1] + 1]
        

if __name__ == "__main__":
    s = Solution()
