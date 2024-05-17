# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        @cache
        def dp(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if (i, j) == (n-1, m-1):
                return 1
            right = down = 0
            if (i+1) < n:
                right =  dp(i+1, j)
            if (j + 1) < m:
                down = dp(i, j+1)
            return right + down
        return dp(0,0)
            

        