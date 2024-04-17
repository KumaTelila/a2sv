# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.nums = nums
        self.k = k
        while len(nums) > k:
            heappop(nums)
        # self.ans = nsmallest(self.k, self.nums)
    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
        

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)