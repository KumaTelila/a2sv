# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incomming = [0]*n

        for u, v in edges:
            graph[u].append(v)
            incomming[v]+=1
        
        queue = deque()
        for i in range(n):
            if incomming[i] == 0:
                queue.append(i)
        
        ans = [set() for _ in range(n)]
        while queue:
            ele = queue.popleft()
            for negh in graph[ele]:
                if ans[ele]:
                    for i in ans[ele]:
                        ans[negh].add(i)
                ans[negh].add(ele)
                incomming[negh]-=1

                if incomming[negh] == 0:
                    queue.append(negh)
        for i in range(n):
            ans[i] = sorted(ans[i])
        return ans

        
        