from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)

        if nt > ns:
            return ""

        t_count = Counter(t)
        # seen = Counter(s)
        # print(tc in seen)
        left = right = 0

        # First, traverse until we reach that t is contained in.
        while ((+t_count).total() != 0 and right < ns):
            if s[right] in t_count:
                t_count[s[right]] -= 1
            right += 1

        if ((+t_count).total() != 0):
            # didn't find a substring of s containing t.
            return ""
        
        min_left = left
        min_right = right


        # From here we try to find the smallest window, whic must be
        # <= size of our current one.
        # While right isn't at the right boundary,
        # OR right *is* but s[left] isn't in t so we can shrink window,
        # OR right *is* but s[left] in t AND t_count[s[left]] < 0 so we
        # can shrink the window.
        while (right < ns - 1) or (right == ns - 1 and \
                ((not s[left] in t_count) or  \
                (s[left] in t_count and t_count[s[left]] < 0))):
            if left == right:
                # only should happen if smallest substring is empty
                return ""
            if (+t_count).total() == 0 and s[left] not in t_count:
                # left is irrelevant so we can shrink there.
                left += 1
            elif (+t_count).total() == 0 and s[left] in t_count and \
                t_count[s[left]] < 0:
                # can still shrink
                t_count[s[left]] += 1
                left += 1
            else:
                # can't shrink from left; move our window over to the
                # right.
                if s[left] in t_count:
                    t_count[s[left]] += 1
                left += 1
                if s[right] in t_count:
                    t_count[s[right]] -= 1
                right += 1
            # since the answer is unique...
            # I suppose we can just do this; but this might be O(n)
            # update to use separate vars instead?
            if (+t_count).total() == 0:
                min_left = left
                min_right = right

        if right == ns - 1 and s[right] in t_count and t_count[s[right]] < 0 and \
                (+t_count).total() == 0:
            t_count[s[right]] -= 1
            right += 1
            min_right += 1
        while (+t_count).total() == 0 and (s[left] not in t_count or \
                t_count[s[left]] < 0):
            if s[left] in t_count:
                t_count[s[left]] += 1
            left += 1
            min_left = left

        return s[min_left: min_right]


        
            

       
if __name__ == "__main__":
    s = Solution()
    # print(s.minWindow("ADOBECODEBANC", "ABC"))
    # print(s.minWindow("a", "a"))
    # print(s.minWindow("a", "aa"))
    print(s.minWindow("bdab", "ab"))
    # print(s.minWindow("bba", "ab"))
    # print(s.minWindow("abcabdebac", "cda"))

                



        