class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0
        pref =0 
        for i in nums:
            pref+=i
            ch = pref- goal
            if ch in dic:
                ans+=dic[ch] 
            dic[pref] +=1
        return ans