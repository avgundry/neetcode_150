class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        s2 = '|' + '|'.join(s) + '|'
        n2 = len(s2)
        best_radius = 0
        for ctr in range(n2):
            # if ctr - best_radius < 0 or ctr + best_radius >= n or \
            if s2[ctr - best_radius:ctr] != s2[ctr + 1:ctr + best_radius + 1]:
                # Cannot be longer than current best palindrome.
                continue
            while ctr - best_radius > 0 and ctr + best_radius < n2 and \
                    s2[ctr - best_radius] == s2[ctr + best_radius]:
                best_radius += 1
                best_ind = ctr

        print(best_radius)
        # Then convert it back...hmmm.
        print(f"Best substring of s2 {s2} is {s2[best_ind- best_radius + 1:best_ind + best_radius]}, centered at index {best_ind}, {s2[best_ind]}")

        return s2
        dp = [1 for _ in range(n)]
        best = 1

        for i in range(1, n):
            left = s[i - best:i]
            right = s[i + 1: i + best + 1]
            while i - best > 0 and i + best < n and left == right:
                best += 1
                dp[i] = best

        best_ind = dp.index(max(dp))
        print(f"best_ind: {best_ind}")
        print(f"best substring: {s[best_ind - best:best_ind + best - 1]}")
        return dp.index(max(dp))

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))


        