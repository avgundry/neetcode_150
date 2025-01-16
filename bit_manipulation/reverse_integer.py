class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if str(x)[0] == '-':
            x = -1 * x
            neg = -1

        val = neg * int(str(x)[::-1])
        if val < (-2)**31 or val > 2 ** 31 - 1:
            return 0
        
        return val
        