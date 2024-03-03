class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = -float('inf')
        curr = 0
        for i in nums:
            curr+=i
            if curr > prev:
                prev = curr
            if curr < 0:
                curr = 0
        return prev
        