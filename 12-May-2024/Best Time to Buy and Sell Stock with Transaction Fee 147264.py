# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -float('inf')
        sell = 0
        for i in prices:
            buy = max(buy, sell - i)
            sell = max(sell, buy + i - fee)
        return sell