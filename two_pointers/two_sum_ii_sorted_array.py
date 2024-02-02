from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1, right + 1]
            elif curr < target:
                left += 1
            else:
                right -= 1

        return None


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
        