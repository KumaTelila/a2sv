# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        for i in range(len(happiness)):
            happiness[i]*=-1
        heapify(happiness)
        minus = 0
        ans = 0
        while k > 0:
            top = -heappop(happiness)
            # print(top, minus)
            if top-minus > 0:
                ans += top - minus
            k -= 1
            minus += 1
        return ans
        