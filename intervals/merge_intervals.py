from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals to make sure we can loop over 
        # and check each pair in order.
        intervals.sort()
        # Initialize output array.
        res = []

        # Loop over and find overlapping intervals at each step.
        for i in range(len(intervals)):
            # If res already has at least one interval in it,
            # and the current interval overlaps with the last interval in res,
            # update the last interval in res to go to the largest of the two interval's
            # endpoints.
            # If we have res[-1] = [1, 4] and intervals[i] = [3, 7], we'd merge the two and get
            # res[-1] = [1, 7].
            if res and intervals[i][0] <= res[-1][1]:
                # We take the max of their endpoints for cases such as
                # res[-1] = [1, 4] and intervals[i] = [2, 3], 
                # where we'd simply keep [1, 4] the same.
                res[-1][1] = max(res[-1][1], intervals[i][1])
            # Otherwise, either res is empty or the intervals are nonoverlapping,
            # so we simply append the current interval to res.
            else:
                res.append(intervals[i])

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[8,10],[15,18], [2,6]]))
    print(s.merge([[1, 4], [4, 5]]))
        