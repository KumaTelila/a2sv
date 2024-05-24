# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(ind, buy):
            if ind >= len(prices):
                return 0
            if buy:
                return max(-prices[ind] + dp(ind + 1, False), dp(ind + 1, True))
            else:
                return max(prices[ind] + dp(ind + 2, True), dp(ind + 1, False))
            # return max(take, nottake)
        ans = dp(0, True)
        return ans 