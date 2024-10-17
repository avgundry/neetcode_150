class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numdict = {str(i): i for i in range(10)}
        m = len(num1)
        n = len(num2)
        nm1 = 0
        nm2 = 0
        for i in range(m - 1, -1, -1):
            nm1 += numdict[num1[i]] * (10 ** (m - 1 - i))
        for j in range(n - 1, -1, -1):
            nm2 += numdict[num2[j]] * (10 ** (n - 1 - j))

        return str(nm1 * nm2)
            
        