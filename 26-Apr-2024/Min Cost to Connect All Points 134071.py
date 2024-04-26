# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        un = UnionFind(len(points))
        ans = 0

        heap = []
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                dist = manhattan(points[i], points[j])
                heap.append((dist, i, j))
        heap.sort()
        queue = deque(heap)
        while queue:
            dist, x, y = queue.popleft()
            if un.find(x) != un.find(y):
                un.union(x, y)
                ans += dist
            # ans+=mn
        return ans

        