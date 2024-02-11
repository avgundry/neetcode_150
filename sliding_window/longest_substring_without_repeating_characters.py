class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n

        left = right = 0 
        seen = set()
        seen.add(s[0])
        best = 0
        while right < n - 1:
            right += 1
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best, len(seen))
            

        return best

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring(" "))
        