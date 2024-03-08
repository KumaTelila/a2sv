class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def partion(mid):
            parts = 1
            sm = 0
            for i in nums:
                if sm + i > mid:
                    sm = 0
                    parts+=1
                sm+=i
            return parts

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low)//2

            parts = partion(mid)

            if parts <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


        