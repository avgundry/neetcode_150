from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Sliding window"""
        n = len(s)

        if n <= 1:
            return n

        left = right = 0
        # notes how many times we've seen each alphabetic character
        # in the current window.
        c = Counter()
        c[s[left]] += 1

        while right < n - 1:
            if c.total() - c.most_common()[0][1] > k:
                c[s[left]] -= 1
                left += 1
                right += 1
                c[s[right]] += 1
            else:
                right += 1
                c[s[right]] += 1

        if c.total() - c.most_common()[0][1] > k:
            c[s[left]] -= 1

        return c.total()


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
    print(s.characterReplacement("AABABBA", 1))


            

        