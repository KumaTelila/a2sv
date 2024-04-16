# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        count = 0
        for i in nums:
            if len(heap) < k:
                heappush(heap, i)
            elif heap[0] < i:
                heapreplace(heap, i)   
        return heap[0]
        