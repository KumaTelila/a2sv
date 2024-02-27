class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = Counter()
        dic[0] = 1
        pref = 0
        ans = 0
        for i in nums:
            pref+=i
            j = pref- k
            if j in dic:
                ans+=dic[j]
            dic[pref]+=1
        return ans

