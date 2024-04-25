# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

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
    def removeStones(self, stones: List[List[int]]) -> int:
        un = UnionFind(len(stones))
        row = {}
        column  = {}
        for i in range(len(stones)):
            r = stones[i][0]
            c = stones[i][1]
            if r in row:
                un.union(i, row[r])
            if c in column:
                un.union(i, column[c])
            row[r] = i
            column[c] = i
        ans = defaultdict(list)
        for i in range(len(stones)):
            ans[un.find(i)].append(i)
        res = 0
        for i in ans:
            res+=len(ans[i]) - 1
        # print(ans)
        return res
        