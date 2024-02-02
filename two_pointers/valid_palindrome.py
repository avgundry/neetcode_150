class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([x.lower() for x in s if x.isalnum()])
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(""))
    print(s.isPalindrome("apa"))
    print(s.isPalindrome("app"))
    print(s.isPalindrome("A man, a plan, a canal: Panama"))

        