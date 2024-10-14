from typing import List


class TrieNode:
    def __init__(self, word):
        # The nodes this points to.
        self.children : dict = dict()
        # Whether this is a 'terminal' node, i.e. whether 
        # any inserted word ends here.
        self.endsWord : bool = len(word) == 1
        # The letter stored in this node.
        self.letter = word[0]
        if len(word[1:]) > 0:
            # Need to create children nodes.
            self.children[word[1]] = TrieNode(word[1:])
    
    def search(self, word):
        if len(word) == 1 and self.endsWord and word[0] == self.letter:
            return True
        elif len(word) == 1 or word[0] != self.letter:
            return False
        if word[1] not in self.children:
            return False
        else:
            return self.children[word[1]].search(word[1:])
    
    def insert(self, word):
        if len(word) == 0:
            raise ValueError('0 len word passed to insert')
        if word[0] != self.letter:
            raise ValueError(f"Should not happen; word[0] {word[0]} != self.letter {self.letter}.")
        word = word[1:]
        if len(word) == 0:
            self.endsWord = True
        elif word[0] not in self.children:
            self.children[word[0]] = TrieNode(word)
        else:
            self.children[word[0]].insert(word)

    def prefix(self, word):
        if len(word) == 1 and word[0] == self.letter:
            return True
        elif len(word) == 1 or word[0] != self.letter:
            return False
        if word[1] not in self.children:
            return False
        else:
            return self.children[word[1]].prefix(word[1:])


class Trie:
    def __init__(self):
        self.root = dict()
        

    def insert(self, word: str) -> None:
        if word[0] in self.root:
            self.root[word[0]].insert(word)
        else:
            self.root[word[0]] = TrieNode(word)

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True
        if word[0] not in self.root:
            return False
        return self.root[word[0]].search(word)

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.root:
            return False
        return self.root[prefix[0]].prefix(prefix)
        
if __name__ == "__main__":
    obj = Trie()
    obj.insert("apple")
    param1 = obj.search("apple")
    param2 = obj.search("app")
    param3 = obj.startsWith("app")
    obj.insert("app")
    param4 = obj.search("app")
    print(f"params: {[param1, param2, param3, param4]}")
    # word = "apple"
    # prefix = "app"
    # obj = Trie()
    # obj.insert(word)
    # param_2 = obj.search(word)
    # param_3 = obj.search(prefix)
    # param_4 = obj.startsWith(prefix)
    # obj.insert(prefix)
    # param_5 = obj.search(prefix)
    # obj.insert("apply")
    # param_6 = obj.search("apply")
    # print('ok')

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)