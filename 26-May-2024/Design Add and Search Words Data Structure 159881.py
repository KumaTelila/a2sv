# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.trie
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]
        temp.is_end = True

    def search(self, word: str) -> bool:
        def dfs(curr,i):
            if i==len(word):
                return curr.is_end
            
            if word[i]=='.':
                for child in curr.children.values():
                    if dfs(child,i+1):
                        return True
                return False

            if word[i] not in curr.children:
                return False
                
            return dfs(curr.children[word[i]],i+1)
  

        return dfs(self.trie,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)