# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def nice(temp):
            st = set(temp)
            ch = ''
            for i in st:
                if i.isupper():
                    ch = i.lower()
                    if ch not in st:
                        return False
                else:
                    ch = i.upper()
                    if ch not in st:
                        return False      
            return True
        ans = ''
        for i in range(len(s)):
            la = len(ans)
            for j in range(i + 1, len(s)):
                temp = s[i:j+1]
                lt = len(temp)
                if nice(temp):
                    if lt > la:
                        ans = temp

        return ans