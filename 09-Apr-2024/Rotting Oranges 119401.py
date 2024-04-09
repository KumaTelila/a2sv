# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        rotten = deque()
        row = len(grid)
        col = len(grid[0])
        fresh_orange = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    fresh_orange += 1
        minutes = 0
        visited = set()
        while rotten and fresh_orange > 0:
            l = len(rotten)
            minutes+=1
            for _ in range(l):
                r, c = rotten.popleft()
                visited.add((r, c))
                for direc in directions:
                    x = r + direc[0]
                    y = c + direc[1]
                    if inbound(x, y) and (x, y) not in visited and grid[x][y] == 1:
                        flag = True
                        rotten.append((x, y))
                        visited.add((x, y))
                        fresh_orange-=1    
        return minutes if fresh_orange < 1 else -1


                

        


        