# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
        self.ans = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        temp = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not temp.children[ind]:
                temp.children[ind] = TrieNode()
            temp = temp.children[ind]
        temp.is_end = True

    def find(self, word):
        temp = self.root
        count = 0
        for ch in word:
            ind = ord(ch) - ord('a')
            if temp and temp.children[ind] and temp.children[ind].is_end == True:
                return word[:count + 1]
            if temp:
                temp = temp.children[ind]
            count += 1
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        ans = []
        for word in dictionary:
            trie.insert(word)
        for word in sentence.split():
            curr = trie.find(word)
            ans.append(curr)
        return ' '.join(ans)
        