class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        dic  = {0: 0, 1:0}
        l = r = 0
        window = 0
        while r<len(nums):
            dic[nums[r]]+=1
            while dic[0] > k:
                dic[nums[l]]-=1
                l+=1
            r+=1
            window = max(window, r - l)
        return window
            
        