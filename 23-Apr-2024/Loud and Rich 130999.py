# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = [[] for i in range(len(quiet))]
        indegree = [0 for i in range(len(quiet))]
        mx = 0
        cur = quiet[0]
        for ind, num in enumerate(quiet):
            if num > cur:
                mx = ind
                cur = num
            # print(ind, num)
        ans = [-1 for _ in range(len(quiet))]
        for u, v in richer:
            graph[u].append(v)
            indegree[v]+=1
        
        queue = deque()
        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        parent = [(quiet[i], i) for i  in range(len(quiet))]
        while queue:
            ele = queue.popleft()
            ans[ele] = parent[ele][1]
            for negh in graph[ele]:
                if parent[ele] < parent[negh]:
                    parent[negh] = parent[ele]
                indegree[negh]-=1
                if indegree[negh] == 0:
                    queue.append(negh)
        return ans
        