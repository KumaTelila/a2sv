class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = Counter()
        window[nums[0]]+=1
        sm = nums[0]
        ans = -float('inf')
        i = 0
        j = 1
        while j < len(nums):
            while len(window) < j -i:
                window[nums[i]] -= 1
                sm-=nums[i]
                if window[nums[i]] == 0:
                    del window[nums[i]]
                i+=1
            window[nums[j]]+=1
            if len(window) == j - i:
                ans = max(ans, sm)
            sm+=nums[j]
            j+=1
        if len(window) == j - i:
            ans = max(ans, sm)
        # ans = max(sm, ans)
        return ans
