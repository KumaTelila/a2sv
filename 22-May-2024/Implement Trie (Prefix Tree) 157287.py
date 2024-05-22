# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:

    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not trie.children[ind]:
                trie.children[ind] = TrieNode()
            trie = trie.children[ind]
        trie.is_end = True
    def search(self, word: str) -> bool:
        trie = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not trie.children[ind]:
                return False
            trie = trie.children[ind]
        return trie.is_end

    def startsWith(self, prefix: str) -> bool:
        trie = self.root
        for ch in prefix:
            ind = ord(ch) - ord('a')
            if not trie.children[ind]:
                return False
            trie = trie.children[ind]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)