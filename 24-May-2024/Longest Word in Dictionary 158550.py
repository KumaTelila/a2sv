# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None]*26

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ls = []
        self.ans = ''
    def insert(self, word):
        temp = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if not temp.children[ind]:
                temp.children[ind] = TrieNode()
            temp = temp.children[ind]
        temp.is_end = True
    def traverse(self, node, curr):
        if not node or not node.is_end:
            return
        if len(curr) > len(self.ls):
            self.ls = curr[:]
        
        for i, child in enumerate(node.children):
            if child:
                self.traverse(child, curr + [chr(i + 97)])
        
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = ''
        temp = trie
        # for child in temp.children:
        #     if child:
        #         ls = trie.traverse(child, '')
        #         print(ls, child)
        #         if len(ls) > len(ans):
        #             ans = ls
        #     temp = child 
         
        for i, child in enumerate(trie.root.children):
            if child:
                trie.traverse(child, [chr(97+i)])
                # if len(ls) > len(ans):
                #     ans = ls
        return ''.join(trie.ls)