# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        un = UnionFind(n)
        edgeList.sort(key = lambda x : x[2])
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key = lambda x : x[2])
        queue = deque(edgeList)
        graph  = defaultdict(set)
        ans = [False for _ in range(len(queries))]
        for i in queries:
            start, end, dist, ind = i
            # print(dist, queue[0],)
            while queue and dist > queue[0][-1]:
                st, ed, val = queue.popleft()
                un.union(st, ed)
            if un.find(start) == un.find(end):
                ans[ind] = True
        return ans
        