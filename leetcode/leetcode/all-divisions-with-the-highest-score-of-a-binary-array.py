class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans = Counter()
        ones = nums.count(1)
        left_zeros = 0
        left_ones = 0
        _max = ones
        ans[0]+= ones
        for i in range(len(nums)):
            if nums[i] == 0:
                left_zeros+=1
            else:
                left_ones+=1
            sm = left_zeros + (ones - left_ones)
            _max = max(sm, _max)
            ans[i+1]+=sm
        return [ i for i, j in ans.items() if j == _max]
        
