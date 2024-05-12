# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_buy = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < curr_buy:
                curr_buy = prices[i]
            ans = max(ans, prices[i] - curr_buy)
        return ans
