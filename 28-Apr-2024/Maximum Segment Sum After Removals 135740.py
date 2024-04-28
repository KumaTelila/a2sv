# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class UnionFind:
    def __init__(self, size):
        self.root = {i : i for i in range(size)}
        self.size = [1] * size
        self.score = defaultdict(int)
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
                self.score[rootX] += self.score[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                self.score[rootY] += self.score[rootX]

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        un = UnionFind(n)
        ans = [0 for i in range(n)]
        d = removeQueries[::-1]
        curr_max = 0
        # print(d)
        for i in range(n):
            ans[i] = curr_max
            mn = d[i] - 1
            mx = d[i] + 1
            # print(un.score)
            un.score[d[i]] = nums[d[i]]
            if mn in un.score:
                un.union(mn, d[i])
            if mx in un.score:
                un.union(mx, d[i])
            curr_max = max(curr_max, un.score[un.find(d[i])])
        ans = ans[::-1]
        return ans