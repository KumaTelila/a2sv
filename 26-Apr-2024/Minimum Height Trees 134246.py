# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        indegree = [0 for i in range(n)]
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
        queue = deque()
        visited = set()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
                visited.add(i)
        ans = defaultdict(list)
        
        count = 1
        while queue:
            l = len(queue)
            for _ in range(l):
                ele = queue.popleft()
                ans[count].append(ele)
                for negh in graph[ele]:
                    indegree[negh] -= 1
                    if negh not in visited and indegree[negh] == 1:
                        queue.append(negh)
                        visited.add(negh)
            count+=1
        mx = -1
        for i in ans:
            if i > mx:
                mx = i
        return ans[mx] 
        