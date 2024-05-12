# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [
            (-1, -1),
            (1, 1),
            (-1, 1),
            (1, -1),
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        ans = [[] for _ in range(len(grid)-2)]
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid)-1):
                curr_max = grid[i][j]
                for x, y in directions:
                    curr_max = max(grid[i+x][j+y], curr_max)
                ans[i-1].append(curr_max)
        return ans


        
