class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        for i in range(len(s)):
            nums[i] = s[i]
        for j in range(i+1, len(nums)):
            nums[j] = 101
        
        return len(s)