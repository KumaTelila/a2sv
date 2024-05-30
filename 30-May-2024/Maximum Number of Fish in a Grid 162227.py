# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def inbound(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return False
            return True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited = set([(r, c)])
            sm = 0
            while queue:
                row, col = queue.popleft()
                sm += grid[row][col]
                for x,  y in directions:
                    newr = x + row
                    newc = y + col
                    if inbound(newr, newc) and (newr, newc) not in visited and grid[newr][newc] > 0:
                        queue.append((newr, newc))
                        visited.add((newr, newc))
            return sm
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    ans = max(ans, bfs(i, j))
        return ans

        