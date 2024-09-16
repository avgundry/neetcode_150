from collections import defaultdict, deque
import heapq
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """BFS approach."""
        queue = [(1, beginWord)]
        wordSet = set(wordList)
        seen = set([beginWord])
        if endWord not in wordSet:
            return 0
        # Hm. If we try to change each character, there's 26m checks,
        # where m is len(beginWord) = len(endWord).
        # If we iterate over each word...for each of n words, we have
        # to iterate over the length of the word to get the total difference.
        # Worst case mn time. So if n > 26 we want to change each character
        # instead.
        # if len(wordList) > 26:
            # Iterate by characters instead.
        alphabet = list(string.ascii_lowercase)
        while queue:
            curr_dist, curr_word = heapq.heappop(queue)
            for i in range(len(curr_word)):
                for letter in alphabet:
                    new_word = curr_word[:i] + letter + curr_word[i + 1:]
                    if new_word in wordSet and new_word not in seen:
                        if new_word == endWord:
                            return curr_dist + 1
                        queue.append((curr_dist + 1, new_word))
                        seen.add(new_word)

        return 0


        """
        Brute force a Dijkstra's approach for now.
        As expected, gets TLE on Leetcode.
        """
        # Construct the adjacency list.
        wordSet = set(wordList)
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return 0
        adj_list = self.adjacency_list(beginWord, endWord, wordList)
        # print(adj_list)

        distances = dict()
        for word in wordSet:
            distances[word] = float('inf')
        distances[beginWord] = 0

        queue = [(0, beginWord)]

        while queue:
            curr_dist, curr_word = heapq.heappop(queue)

            # If a shorter path to the current node has been found, don't process it.
            if curr_dist > distances[curr_word]:
                continue

            # Otherwise, iterate over each neighbor of the current node.
            for neighbor, weight in adj_list[curr_word].items():
                dist = curr_dist + weight

                # Only consider path if it's better than any path previously found.
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(queue, (dist, neighbor))

        out = distances[endWord]
        return out if out != float('inf') else 0
    
    def adjacency_list(self, beginWord, endWord, wordList):
        adj_list = defaultdict(dict)
        wordList = [beginWord] + wordList
        # Could definitely be optimized by checking only letters available
        # in each index.
        # wordSet.add(beginWord)
        # wordSet.add(endWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                word = wordList[i]
                word2 = wordList[j]
                if self.wordDist(word, word2) == 1:
                    adj_list[word][word2] = adj_list[word2][word] = 1
        return adj_list

    def wordDist(self, word1, word2):
        # Returns the distance between two words.
        total = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                total += 1
        return total

if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # should return 5
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) # Should return 0
