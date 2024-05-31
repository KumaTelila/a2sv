# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        new = [[] for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                new[j].append(i)
        incomming = [0] * len(graph)
        for i in range(len(graph)):
            incomming[i] = len(graph[i])
        
        queue = deque()
        for i in range(len(graph)):
            if incomming[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            course = queue.popleft()
            ans.append(course)

            for negh in new[course]:
                incomming[negh]-=1
                if incomming[negh] == 0:
                    queue.append(negh)
        ans.sort()
        return ans

            