from collections import defaultdict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # Hmm. Let dp[key1][key2] be minDistance to go from key1 to key2.
        dp = defaultdict(dict)
        dp[""][""] = 0
        dp[word1][word1] = 0
        dp[word2][word2] = 0

        self.dfs(word1, word2, dp)
        return dp[word1][word2]

    def dfs(self, word1, word2, dp):
        m = len(word1)
        n = len(word2)
        if m == 0 or n == 0:
            dp[word1][word2] = abs(m - n)
        elif dp.get(word1) is not None and dp[word1].get(word2) is not None:
            pass
        elif word1[0] == word2[0]:
            dp[word1][word2] = self.dfs(word1[1:], word2[1:], dp)
        else:
            dp[word1][word2] = 1 + min(
                self.dfs(word2[0] + word1, word2, dp), # Insert option
                self.dfs(word1[1:], word2, dp), # Delete option
                self.dfs(word2[0] + word1[1:], word2, dp) # Replace option
            )
        return dp[word1][word2]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("", ""))
    print(s.minDistance("horse", "ros"))
    print(s.minDistance("intention", "execution"))
    print(s.minDistance("sea", "eat"))