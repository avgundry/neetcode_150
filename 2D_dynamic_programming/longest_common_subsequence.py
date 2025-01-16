import collections

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """DP approach."""
        m = len(text1)
        n = len(text2)
        if m == 0 or n == 0:
            return ""
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

        # def LCS(dp, text1, text2, i, j):
        #     i = len(text1)
        #     j = len(text2)
        #     print(text1)
        #     print(text2)
        #     if i == 0 or j == 0:
        #         return ""
        #     elif text1[i] == text2[j]:
        #         return LCS(text1[:-1], text2[:-1])
        #     else:
        #         return LCS(max(LCS(text1, text2[:-1]), LCS(text1[:-1], text2), key=len))

        # dp = [["" for _ in range(m)] for _ in range(n)]
        # return len(LCS(text1, text2))
            

            
        # Let dp[i][j] be the longest common subsequence of
        # text1[:i] and text2[:j]. 
        # Since LCS(X + A, B + A) = LCS(X, B) + A, we can work backwards until we
        # find mismatched characters between the two texts.
        j = 1
        while j < min(m, n) + 1 and text1[-j] == text2[-j]:
            j -= 1
        # for j in range(-1, min(m, n), -1):
        #     if text1[j] != text2[j]:
        #         break
        # Then we know the characters text1[j:] and text2[j:] are the same.
        suffix = text1[j:]
        text1 = text1[:j]
        text2 = text2[:j]
        print(suffix)
        print(text1, text2)
        return
        # dp = [[0 for _ in range(m)] for _ in range(n)]
        # dp[0][0] = text1[0] == text2[0]
        # for i in range(m):
        #     for j in range(n):
        #         dp[i][j] = 0

        # return dp[m - 1][n - 1]


        # Is there any way to do this that's not O(2^n) time?
        """Brute force approach: generate every subsequence and take the union."""
        m = len(text1)
        n = len(text2)
        # Generate all subsequences for each string.
        subseqs1 = collections.deque([()])
        subseqs2 = collections.deque([()])

        for char in text1:
            currlen = len(subseqs1)
            for i in range(currlen):
                subseqs1.append(subseqs1[i] + (char,))
        for char in text2:
            currlen = len(subseqs2)
            for i in range(currlen):
                subseqs2.append(subseqs2[i] + (char,))

        # We need to look at what work is repeatedly being done.
        intersection = list(set(subseqs1) & set(subseqs2))

        return(len(max(intersection, key=lambda x: len(x))))

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))


        