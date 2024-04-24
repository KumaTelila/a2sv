# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        preq = [set() for i in range(numCourses)]
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        # print(queue, graph)
        while queue:
            ele = queue.popleft()
            for negh in graph[ele]:
                preq[negh].add(ele)
                preq[negh] |= preq[ele] 
                indegree[negh]-=1
                if indegree[negh] == 0:
                    queue.append(negh)
        ans = []
        for a, b in queries:
            if b in preq[a]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        