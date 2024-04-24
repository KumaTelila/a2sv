# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        root = [i for i in range(n+1)]
        size = [1] * (n+1)
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        top = float('inf')
        def union(x, y, dist):
            nonlocal top
            rootX = find(x)
            rootY = find(y)
            top = min(top, dist)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]

        for start, end, dist in roads:
            union(start, end, dist)
        # print(root)
        ans = float('inf')
        for start, end, dist in roads:
            if root[start] == root[1] or root[end] == root[1]:
                ans = min(ans, dist)
        return ans if root[1] == root[n] else top

