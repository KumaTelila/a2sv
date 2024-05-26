# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        comb = [(capital[i], profits[i]) for i in range(n)]
        comb.sort()
        i = 0
        mx = []
        while k > 0:
            while i < n and comb[i][0] <= w:
                heapq.heappush(mx, -comb[i][1])
                i += 1
            if not mx:
                break
            w -= heapq.heappop(mx)
            k -= 1
        return w