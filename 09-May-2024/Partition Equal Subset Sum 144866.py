# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        # ans = False
        # def dp(ind, path = [], sm = 0, seen = set()):
        #     nonlocal ans
        #     # print(sm, path)
        #     if sum(path) > half:
        #         return
        #     if sum(path) == half:
        #         ans =  True
        #         return
        #     for i in range(ind, len(nums)):
        #         if i not in seen:
        #             path.append(nums[i])
        #             seen.add(i)
        #             sm += nums[i]
        #             dp(ind + 1)
        #             ele = path.pop()
        #             sm -= ele
        #             seen.remove(i)
        if half != int(half):
            return False
        memo = {}
        def dp(ind, target):
            if target < 0 or ind >= len(nums):
                return False
            if target == 0:
                return True
            if (ind, target) not in memo:
                memo[(ind, target)] = (dp(ind + 1, target - nums[ind]) or dp(ind+1, target))
            return memo[(ind, target)]

        return dp(0, half)
        # return ans

            


            
        