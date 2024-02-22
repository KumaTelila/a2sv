class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        _min = nums[0]
        ans = 0
        plus = 0
        for i in nums:
            if i > _min:
                _min = i
                plus+=1
            ans+=plus  
        return ans
        