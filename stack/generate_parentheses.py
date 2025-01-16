from collections import deque
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        strings = set()
        dp = dict()
        self.recur_parenthesis(n, "", strings)
        return list(strings)

    def recur_parenthesis(self, n, path, strings, dp):
        if n == 0:
            strings.add(path)
            return
        elif dp.get(path):
            return
        
        p = len(path)
        for i in range(p + 1):
            for j in range(i, p + 1):
                newpath = path[:i] + "(" + path[i:j] + ")" + path[j:]
                self.recur_parenthesis(n - 1, newpath, strings)


        # stack = deque()
        # stack.append("()")
        # for i in range(n - 1):
        #     stacklen = len(stack)
        #     for j in range(stacklen):
        #         curr = stack.popleft()
        #         for k in range(len(curr)):
        #             currcpy = curr[:k] + "(" + curr[k:]
        #             for h in range(k, len(currcpy)):
        #                 stack.append(currcpy[:h] + ")" + currcpy[h:])

        # return list(set(stack))

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(5))
    print(s.generateParenthesis(6))
    print(s.generateParenthesis(7))



        