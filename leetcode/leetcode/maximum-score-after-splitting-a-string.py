class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        ans = 0
        for num in range(len(s)-1):
            if s[num] == '1':
                ones-=1
            else:
                zeros+=1
            ans = max(ans, zeros + ones)
        return ans
            
        