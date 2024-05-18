# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        memo = {}
        def dp(i, j):
            if i == n:
                return True
            if j == m:
                return False
            if (i,j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] =  dp(i+1, j+1)
                return memo[(i, j)]
            memo[(i, j)] =  dp(i, j+1)
            return memo[(i, j)]
        return dp(0, 0)
        