class Solution:
    def getDivisor(self, nums, k):
        divisor = 0
        for num in nums:
            divisor += (ceil(num/k))
        return divisor
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low <=  high:
            mid = low + (high - low)//2
            current_sum = self.getDivisor(nums, mid)
            if current_sum  > threshold:
                 low = mid + 1
            else: 
                high = mid - 1     
        return low
        