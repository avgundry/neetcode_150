class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        left = -1
        maxlen = 0
        seen = set()

        for right, char in enumerate(word):
            if right > 0 and char < word[right - 1]:
                seen = set()
                left = right - 1
            seen.add(char)

            if len(seen) == 5:
                maxlen = max(maxlen, right - left)

        return maxlen
        
        

if __name__ == "__main__":
    s = Solution()
    print(s.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))