# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
        def dp(ind, _sum):
            if _sum == 0:
                return 1
            if ind >= len(coins):
                return 0
            if (ind, _sum) in memo:
                return memo[(ind, _sum)]
            inc = 0
            if _sum >= coins[ind]:
                inc = dp(ind, _sum - coins[ind])
            exc = dp(ind + 1, _sum)
            memo[(ind, _sum)] =  inc + exc
            return memo[(ind, _sum)]
        ans = dp(0, amount)
        return ans

        