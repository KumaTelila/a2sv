# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        n = len(grid)
        path = defaultdict(tuple)
        found = False
        while queue:
            r, c = queue.popleft()
            if grid[r][c] == 1:
                break
            if (r, c) == (n-1, n-1):
                found = True
                break
            for x, y in directions:
                if inbound(x + r, c + y) and (x + r, c + y) not in visited and grid[x + r][c + y] == 0:
                    path[(x + r, c + y)] = (r, c)
                    queue.append((x + r, c + y))
                    visited.add((x + r, c + y))
        count = 1
        ele = (n-1, n-1)
        while ele != (0, 0) and found:
            ele = path[ele]
            count+=1
        return count if found else -1

