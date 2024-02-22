class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        ans = 0
        for i in range(len(nums)-2, -1, -1):
            if prev >= nums[i]:
                prev = nums[i]
                continue
            number_of_slot = ceil(nums[i]/prev)
            ans+=(number_of_slot-1)
            prev = nums[i]//number_of_slot
        return ans


            



        