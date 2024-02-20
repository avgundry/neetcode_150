from collections import deque
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        class ParenStr:
            def __init__(self, st, open_pars, closed_pars):
                self.st = st
                self.open = open_pars
                self.closed = closed_pars
        # Perhaps like this...?
        dq = deque()
        s = '(' * n
        dq.append(s)
        print(dq)
        ret = []
        while dq:
            currlen = len(dq)
            for i in range(currlen):
                for 
        # stack = ['(' * n]
        # while stack:

        # for i in range(n):
        #     pass


if __name__ == "__main__":
    s = Solution()
    # print(s.generateParenthesis(1))
    print(s.generateParenthesis(3))
        