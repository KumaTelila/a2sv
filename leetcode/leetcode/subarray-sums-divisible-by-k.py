class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = Counter()
        dic[0] = 1
        ans = 0
        pref = 0
        for i in nums:
            pref+=i
            j = pref%k
            if j in dic:
                ans+=dic[j]
            dic[j]+=1
        return ans
            
        