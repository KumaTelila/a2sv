# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        un = UnionFind(n)
        for u, v in edges:
            un.union(u, v)
        parents = defaultdict(int)
        for i in range(n):
            p = un.find(i)
            parents[p] += 1
        if not edges:
            return n*(n - 1)//2
        if len(parents) == 1:
            return 0
        ans = 0
        elements = list(parents.values())
        elements.sort(reverse = True)
        suff = [elements[-1]]
        for i in range(len(elements)- 2, 0, -1):
            suff.append(suff[-1] + elements[i])
        suff.reverse()
        for i in range(len(suff)):
            curr = suff[i]*elements[i]
            ans += curr
        return ans

        