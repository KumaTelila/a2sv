# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        temp = tickets[k]
        ans = 0
        cnt = 0
        for i in range(k + 1,len(tickets)):
            if tickets[i] >= temp:
                cnt += 1

        for i in tickets:
            if i < temp:
                ans += i
            else:
                ans += temp
           
        return ans - cnt
