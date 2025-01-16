class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Hmmm. Do some weird loop and carry thing?
        bin_a = bin(a)[::-1]
        bin_b = bin(b)[::-1]
        longer = bin_b if len(bin_b) > len(bin_a) else bin_a
        m = max(len(bin_a), len(bin_b)) - 2
        n = min(len(bin_a), len(bin_b)) - 2
        carry = 0
        out = ''
        for i in range(n):
            if carry == 0:
                if bin_a[i] == '0' and bin_b[i] == '0':
                    out = '0' + out
                elif (bin_a[i] == '1' and bin_b[i] == '0') or (bin_a[i] == '0' and bin_b[i] == '1'):
                    out = '1' + out
                elif bin_a[i] == '1' and bin_b[i] == '1':
                    out = '1' + out
                    carry = 1
                else:
                    print("BUG")
            else:
                if bin_a[i] == '0' and bin_b[i] == '0':
                    out = '1' + out
                    carry = 0
                else:
                    out = '1' + out

        for j in range(n, m):
            if carry == 0:
                out = longer[j:m] + out
                break
            else:
                if longer[i] == '0':
                    carry = 0
                out = '1' + out

        if carry == 1:
            out  = '1' + out

        return int(out, 2)
                

        

if __name__ == "__main__":
    s = Solution()
    print(s.getSum(1, 2))
    print(s.getSum(2, 3))