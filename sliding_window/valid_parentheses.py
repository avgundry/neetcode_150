class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        maps = {'}': '{', ']': '[', ')': '('}

        for i in range(n):
            if s[i] in maps.keys() and (not stack or stack[-1] != maps[s[i]]):
                return False
            elif s[i] in maps.keys():
                stack.pop()
            else:
                stack.append(s[i])

        return (stack == [])

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
