# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        indegrees = [0 for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegrees[v]+=1
        queue = deque()
        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)
        print(list(queue))
        if len(queue) == 1:
            return queue[0]
        return -1
        