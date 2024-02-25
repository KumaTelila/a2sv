class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(pref[-1] + nums[i])
        tot = pref[-1]
        for i in range(len(nums)):
            if tot - pref[i] == pref[i] - nums[i]:
                return i
        return -1
        