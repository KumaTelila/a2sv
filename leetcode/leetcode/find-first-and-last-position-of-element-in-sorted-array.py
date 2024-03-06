class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                if nums[low] < target:
                    low+=1
                if nums[high] > target:
                    high-=1
                if nums[low] == target and nums[high] == target:
                    return [low, high]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > high:
            return [-1, -1]
         