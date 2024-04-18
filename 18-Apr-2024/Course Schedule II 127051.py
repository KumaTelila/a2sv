# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]for i in range(numCourses)]
        incomming = [0 for i in range(numCourses)]
        queue = deque()
        for course, pre in prerequisites:
            graph[pre].append(course)
            incomming[course]+=1
            
        for course in range(numCourses):
            if incomming[course] == 0:
                queue.append(course)
        ans = []
        while queue:
            course = queue.popleft()
            ans.append(course)

            for negh in graph[course]:
                incomming[negh]-=1
                if incomming[negh] == 0:
                    queue.append(negh)
        return ans if len(ans) == numCourses else []


        