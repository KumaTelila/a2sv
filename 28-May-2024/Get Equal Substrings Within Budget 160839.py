# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        ans = 0
        l = 0
        r = 0
        while r < len(s):
            if maxCost < 0:
                maxCost += costs[l]
                l+=1
            else:
                ans = max(ans, r - l)
                maxCost -= costs[r]
                r+=1
        if maxCost >= 0:
            ans = max(ans, r - l)
        return ans
        