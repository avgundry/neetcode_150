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

        # loop until first time t in s[L:R]. 
        # if not, then return false
        while (+t_count).total() != 0 and right < ns:
            if s[right] in t_count:
                t_count[s[right]] -= 1
            right += 1

        if (+t_count).total() != 0:
            return ""

        min_left = 0
        min_range = right - left

        # Loop until right is at the very end of list
        while right < ns:
            if left == right:
                return ""
            if (+t_count).total() == 0:
                # try to shrink.
                if s[left] in t_count and t_count[s[left]] < 0:
                    t_count[s[left]] += 1
                    # min_left = left
                elif s[left] in t_count:
                    if s[right] in t_count:
                        t_count[s[right]] -= 1
                    right += 1
                    t_count[s[left]] += 1
                # elif s[left] not in t_count:
                #     left += 1
                # else:
                #     right += 1
                # min_range = right - left
                left += 1
                if (right - left) < min_range:
                    min_range = right - left
                    min_left = left
            else:
                left += 1
                right += 1

        # SO close. Where am I going wrong
        if (+t_count).total() == 0:
            while left < right and (s[left] not in t_count or \
                (s[left] in t_count and t_count[s[left]] < 0)):
                if s[left] in t_count and t_count[s[left]] < 0:
                    t_count[s[left]] += 1
                left += 1
                min_left = left
                min_range = right - left

        

        return s[min_left: min_left + min_range]

       
if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "a"))
    print(s.minWindow("a", "aa"))
    print(s.minWindow("bdab", "ab"))
    print(s.minWindow("bba", "ab"))
    print(s.minWindow("abcabdebac", "cda"))

                



        