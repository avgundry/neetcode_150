from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # The first partition will always just be each individual character.
        partitions = [] 
        self.find_palindrome([], s, partitions)
       
        return partitions

    def find_palindrome(self, curr, remain, partitions):
        """
        curr is the list containing the current partition.
        remain is the remaining string, after curr's characters are removed from s.
        partitions is the list of partitions which will be appended to if a valid
            partition is found.
        """
        if remain == "":
            partitions.append(curr)
        for i in range(1, len(remain) + 1):
            # if s[i:]
            pass

        print(curr)
        print(remain)
        print()

    def is_palindromic(self, strings):
        for s in strings:
            if s != s[::-1]:
                return False
        return True



if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))