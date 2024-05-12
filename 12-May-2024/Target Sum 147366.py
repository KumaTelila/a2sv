# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(ind, _sum):
            if ind == len(nums):
                return 1 if _sum == target else 0
            if (ind, _sum) in memo:
                return memo[(ind, _sum)]
            memo[(ind, _sum)] = backtrack(ind + 1 , _sum + nums[ind]) + backtrack(ind + 1, _sum - nums[ind])  
            return memo[(ind, _sum)]
        return backtrack(0, 0)

        