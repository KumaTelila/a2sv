class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dic = {0: 0, 1: 0}
        ans = 0
        l = 0
        r = 0
        while r < len(nums):
            dic[nums[r]]+=1
            if dic[0] > 1:
                dic[nums[l]]-=1
                l+=1
            if dic[0] == 1:
                ans = max(ans, dic[1])
            if dic[0] == 0:
                ans = max(ans, dic[1]-1)
            r+=1
        return ans
        