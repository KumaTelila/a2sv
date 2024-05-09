# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(step):
            # if n <= 2:
            #     return n
            # if n in memo:
            #     return memo[n]
            # memo[n] = dp(n-1) + dp(n-2)
            # return memo[n]
            if step > n:
                return 0
            if step == n:
                return 1
            if step in memo:
                return memo[step]
            memo[step] = dp(step + 1) + dp(step + 2)
            return memo[step]
        return dp(0)
