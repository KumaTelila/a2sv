# Problem: Max Numbers of K sums - https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            curr = nums[l] + nums[r]
            if curr == k:
                count += 1
                l += 1
                r -= 1
            elif curr < k:
                l += 1
            else:
                r -= 1
        return count
        