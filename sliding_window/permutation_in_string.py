from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n2 = len(s2)
        if n2 < len(s1):
            return False

        c1 = Counter(s1)

        left = 0
        right = 0
        while right < n2:
            if s2[right] in c1 and c1[s2[right]] > 0:
                c1[s2[right]] -= 1
                right += 1
            elif s2[left] in c1:
                c1[s2[left]] += 1
                left += 1
            elif left == right:
                right += 1
            else:
                left +=1 

            if c1.total() == 0:
                return True
        
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("ab", "eidboaoo"))
    print(s.checkInclusion("adc", "dcda"))
