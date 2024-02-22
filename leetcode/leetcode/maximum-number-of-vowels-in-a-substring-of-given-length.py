class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ls = []
        j = 0
        c = 0
        m = 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                c+=1
            if i-j+1 == k:
                m = max(m, c)
                if s[j] in "aeiou":
                    c-=1
                j+=1
        return m


