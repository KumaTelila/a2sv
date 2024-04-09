# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        queue = deque()
        queue.append(0)
        visited[0] = True
        while queue:
            ele = queue.popleft()
            for key in rooms[ele]:
                if not visited[key]:
                    queue.append(key)
                    visited[key] = True
        ans = visited.count(False)
        return ans == 0
        