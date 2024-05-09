# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        ans = 0
        for i in nums:
            if (xor & -xor) & i == 0:
                ans ^= i

        return [xor ^ ans, ans]
        