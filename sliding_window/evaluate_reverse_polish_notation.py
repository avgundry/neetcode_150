import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # """Two-pointer method"""
        # Not sure if possible actually. Might need to work backwards
        # instead, but I'm not sure if that's permissible under RPN
        # n = len(tokens)
        # if n <= 2:
        #     return int(tokens[0])
        
        # curr1 = int(tokens[0])
        # curr2 = int(tokens[1])
        # for i in range(2, n):
        #     if tokens[i] == '+':
        #         curr1 = curr1 + curr2
        #     elif tokens[i] == '-':
        #         curr1 = curr2 - curr1
        #     elif tokens[i] == '*':
        #         curr1 *= curr2
        #     elif tokens[i] == '/':
        #         curr1 = curr2 // curr1
        #     else:
        #         curr2 = int(tokens[i])

        # return curr1


        """Stack method"""
        stack = []
        n = len(tokens)

        for i in range(n):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                stack.append(-(stack.pop()) + stack.pop())
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == '/':
                stack.append(math.floor((1 / stack.pop()) * stack.pop()))
            else:
                stack.append(int(tokens[i]))

        return stack[0]

if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2","1","+","3","*"]))
        