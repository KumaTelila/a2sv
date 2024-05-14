# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            return True

        memo = {}
        def dp(i, j):
            if (i, j) == (m-1, n-1):
                return 1
            if not inbound(i, j):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            down = dp(i + 1, j)
            right = dp(i, j + 1)
            memo[(i, j)] = down + right
            return memo[(i, j)]
        ans = dp(0, 0)
        return ans

