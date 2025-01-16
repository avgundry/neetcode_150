class Solution:
    def reverseBits(self, n: int) -> int:
        return int(reversed((bin(n)[2:])))

if __name__ == "__main__":
    s = Solution()
    
        