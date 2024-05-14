# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(ind, _sum):
            if _sum == 0:
                return 1
            if ind >= n:
                return 0
            if (ind, _sum) in memo:
                return memo[(ind, _sum)]
            inc = 1
            if _sum >= ind:
                inc = ind * dp(ind, _sum - ind)
            exc = dp(ind + 1, _sum)
            memo[(ind, _sum)] =  max(inc, exc)
            return memo[(ind, _sum)]
        ans = dp(1, n)
        return ans
