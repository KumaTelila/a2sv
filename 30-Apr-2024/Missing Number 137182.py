# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        _xor = 0
        for i in range(n+1):
            _xor ^= i
        for num in nums:
            _xor ^= num
        return _xor