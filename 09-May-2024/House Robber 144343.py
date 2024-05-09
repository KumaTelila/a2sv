# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # ans = 0
        memo = {}
        def dp(ind, ans = 0):
            # nonlocal ans
            if ind >= len(nums):
                return 0
            if ind in memo:
                return memo[ind]
            memo[ind] = max(nums[ind] + dp(ind+2), dp(ind+1))
            return memo[ind]
            # return ans
        return dp(0)
        # return 0
        