# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(x):
            if x == 0:
                return 0
            if x < 0:
                return 1000000
            ans = 1000000
            for i in coins:
                ans = min(ans, dp(x - i) + 1)
            return ans
        ans = dp(amount)
        return -1 if ans == 1000000 else ans
        