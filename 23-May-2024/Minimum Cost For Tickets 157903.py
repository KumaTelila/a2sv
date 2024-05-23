# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1] + 1)
        for day in days:
            for i in range(days[-1] + 1):
                if i > day:
                    dp[i] = dp[i - 1]
                else:
                    dp[day] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        
        # print(dp)
        return dp[-1]
                
        