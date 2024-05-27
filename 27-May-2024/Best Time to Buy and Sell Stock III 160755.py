# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for i in range(3)]for j in range(2)]
        curr=[[0 for i in range(3)]for j in range(2)]
        for buy in range(2):         
            for cap in range(3):
                curr[buy][cap]=0
        for ind in range(n):          
            for buy in range(2):
                curr[buy][0]=0

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy==1:
                        curr[buy][cap]=max(-prices[ind]+dp[0][cap],0+dp[1][cap])
                    else:
                        curr[buy][cap]=max(prices[ind]+dp[1][cap-1],0+dp[0][cap])
            dp=curr
        return dp[1][2] 