# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        un = UnionFind(len(s))
        for i, j in pairs:
            un.union(i, j)
        ls = []
        for i in s:
            ls.append(i)
        group = defaultdict(list)
        indexs = defaultdict(list)
        for i in range(len(s)):
            parent = un.find(i)
            group[parent].append(ls[i])
            indexs[parent].append(i)
        for i in group:
            group[i] = sorted(group[i])
        ans = ['' for i in range(len(s))]
        for i in group:
            for j in range(len(group[i])):
                ind = indexs[i][j]
                ans[ind] = group[i][j]
        return ''.join(ans)