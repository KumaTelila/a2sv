class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ls = ['']*len(strs[0])
        for i in strs:
            for j in range(len(i)):
                ls[j]+=i[j]
        ans = 0
        for i in ls:
            s = ''.join(sorted(i))
            if i != s:
                ans+=1
        return ans
        