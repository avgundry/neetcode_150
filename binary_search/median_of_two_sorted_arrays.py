import bisect
import heapq
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search solution.
        """
        m = len(nums1)
        n = len(nums2)
        w = m + n
        target = w // 2

        if m == n == 0:
            return None
        elif m == 0:
            if n % 2 == 0:
                return nums2[n // 2 - 1] / 2 + nums2[n // 2] / 2 
            else:
                return nums2[n // 2]
        elif n == 0:
            if m % 2 == 0:
                return nums1[m // 2 - 1] / 2 + nums1[m // 2] / 2
            else:
                return nums1[m // 2]


        # So what we want is to find the index (m + n) // 2 in the sorted array.
        # We can set up an array tracking elems to the left in one array and binary search.
        # tracks elements to the left of element [i] in nums1
        left_numcount = [0 for _ in range(m)]
        # Binary search nums2 for where nums1[-1] would slot in, lets us 
        # set last element of left_numcount.
        left_numcount[-1] = bisect.bisect_left(nums2, nums1[-1])
        left_numcount[0] = bisect.bisect_left(nums2, nums1[0])
        print(left_numcount)
        if left_numcount[0] == target:
            return nums1[0]
        elif left_numcount[-1] == target:
            return nums1[-1]
        # can easily just treat as one large sorted array in these two cases.
        # elif (left_numcount[-1] == 0 and target >= m) or (left_numcount[0] == n and target < n):
        #     # Search only in nums2
        #     if w % 2 == 0:
        #         return nums2[(target - m) - 1] / 2 + nums2[target - m] / 2
        #     else:
        #         return nums2[target - m]
        # elif (left_numcount[-1] == 0 and target < m) or (left_numcount[0] == n and target >= n):
        #     # Search only in nums1
        #     if w % 2 == 0:
        #         return nums1[(target - n) - 1] / 2 + nums1[target - n] / 2
        #     else:
        #         return nums1[target - n]

        left = 0
        right = m - 1
        curr = left + right // 2
        while curr != target and left < right and not (target > left_numcount[curr] and target < left_numcount[curr + 1]):
            if curr < target:
                left = curr + 1
            elif curr > target:
                right = curr

        if curr == target:
            if w % 2 == 0:
                if curr - 1 > 0:
                    return nums1[curr - 1] / 2 + nums1[curr] / 2
                else:
                    return nums1[curr] / 2 + nums2[-1] / 2
            else:
                return nums1[curr]


        if curr == target:
            return nums1[curr]

        # Otherwise, binary search through nums2?
        left = left_numcount[curr]
        right = left_numcount[curr - 1]


        # """
        # Begin with the brute force solution: merge the two arrays into one sorted one.
        # """
        # # Let's see...
        # if len(nums1) == 0 and len(nums2) == 0:
        #     return None

        # newnums = sorted(nums1 + nums2)
        # # while len(nums1) > 0 and len(nums2) > 0
        # n = len(newnums)
        # if n % 2 == 0:
        #     return newnums[n // 2 - 1] / 2 + newnums[n // 2] / 2
        # else:
        #     return newnums[n // 2]


if __name__ == "__main__":
    s = Solution()
    # print(s.findMedianSortedArrays([1, 3], [2]))
    # print(s.findMedianSortedArrays([1, 3], [2, 4]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    # print(s.findMedianSortedArrays([1], []))
    # print(s.findMedianSortedArrays([], []))
        