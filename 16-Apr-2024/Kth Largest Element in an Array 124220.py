# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = heappop(nums)
        l = len(nums)
        for _ in range(l - k+1):
            ans = heappop(nums)
        return ans