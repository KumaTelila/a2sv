# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = defaultdict(str)
        def find(x):
            if root[x] =='':
                root[x] = x
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rootX < rootY:
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
        for i in range(len(s1)):
            union(s1[i], s2[i])
        ans = ''
        for i in baseStr:
            ans+=find(i)
        return ans
                    