import collections


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        elif s[0] == '0':
            # Nonvalid character.
            return 0
        # number of paths up to s[:i]
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 1
        # dp[1] = 1
        
        self.decode(s, dp, 1)
        return dp[-1]

    def decode(self, s, dp, ind):
        if ind > len(s):
            # Got to end of a valid path.
            return 1
        total = 0
        if s[ind - 1] != '0':
            total += dp[ind - 1]
        if ind > 1 and int(s[ind - 2:ind]) <= 26 and s[ind - 2] != '0':
            total += dp[ind - 2]
        dp[ind] = total
        self.decode(s, dp, ind + 1)



if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("11106"))
    print(s.numDecodings("06"))
    print(s.numDecodings("226"))
