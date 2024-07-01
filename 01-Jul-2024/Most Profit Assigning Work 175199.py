# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combination = [(difficulty[i], profit[i]) for i in range(len(profit))]
        combination.sort()
        worker.sort()
        ans = 0
        i = 0
        j = 0
        prof = 0
        while i < len(worker):
            while j < len(profit) and combination[j][0] <= worker[i]:
                prof = max(prof, combination[j][1])
                j += 1
            # print(worker[i], prof)
            ans += prof
            i += 1
        
        # print(combination, worker, ans, i)
        return ans
        