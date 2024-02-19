class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        sm = len(nums)
        if sum(nums)<target:
            return 0
        _sum = 0
        for i in range(len(nums)):
            _sum+=nums[i]
            print(_sum)
            while _sum >= target:
                sm = min(sm, i+1-j)
                _sum-=nums[j]
                j+=1
        return sm