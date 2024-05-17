# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        directions = [(1, -1), (1, 0), (1, 1)]
        n = len(matrix)
        memo = {}
        def inbound(row, col):
            if row < 0 or col < 0 or row >= n or col >= n:
                return False
            return True
        def dp(i, j):
            if i == n - 1:
                return matrix[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            take = float('inf')
            for x, y in directions:
                if inbound(i+x, j+y):
                    take = min(dp(i+x, j+y) + matrix[i][j], take)
                    memo[(i, j)] = take
            return memo[(i, j)]
        ans = float('inf')
        for i in range(n):
            ans = min(ans, dp(0, i))
        return ans
        
            

        