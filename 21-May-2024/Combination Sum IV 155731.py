# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        # n = len(nums)
        # dp = [0 for i in range(target + 1)]
        # dp[0] = 1
        # for num in nums:
        #     for i in range(num, target + 1):
        #         dp[i] = dp[i - num]
        @cache
        def dp(sm):
            if sm == 0:
                return 1
            if sm < 0:
                return 0
            take = 0
            for i in range(len(nums)):
                if nums[i] <= sm:
                   take += dp(sm - nums[i])
                else:
                    return take
            return take
        ans = dp(target)
        return ans
            
        #     # for i in range(len(nums)):
        #     #     take = 0
        #     #     if sm >= nums[i]:
        #     #         take = dp(i, sm - nums[i])
        #     #     return  + dp(i + 1, sm)
        #     # take = 0
        #     # if sm >= nums[ind]:
        #     #     path.append(nums[ind])
        #     #     take = dp(ind, sm - nums[ind], path)
        #     #     if path:
        #     #         path.pop()
        #     # nottake = dp(ind + 1, sm, path)
        #     # return take + nottake
        # return dp(target)
        # ans = 0
        # # @cache
        # def backtrack(ind, sm):
        #     nonlocal ans
        #     if sm == target:
        #         # ans+=1
        #         return 1
        #     if sm > target:
        #         return 0
        #     for i in range(len(nums)):
        #         # path.append(nums[i])
        #         sm += nums[i]
        #         x =  backtrack(i+1, sm)
        #         if x:
        #             return x + 1
        #         # ele = path.pop()
        #         sm -= nums[i]
        #     return 0
        # ans = backtrack(0, 0)
        return ans
            