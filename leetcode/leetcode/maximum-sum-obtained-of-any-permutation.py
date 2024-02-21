class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mdl = 10**9 + 7
        pref = [0]*(len(nums)+1)
        for i, j in requests:
            pref[i]+=1
            pref[j+1]-=1
        for i in range(1, len(pref)):
            pref[i]+=pref[i-1]
        pref.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0
        for i in range(len(nums)):
            ans  += (nums[i]*pref[i])%mdl
        print(pref)
        return ans%mdl
        