# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def check(s, ind):
            num = 0
            while ind < len(s):
                if s[ind] == '.':
                    break
                else:
                    num = num * 10 + int(s[ind])
                ind+=1
            return [num, ind+1]
        i = j = 0
        while i < len(version1) or j < len(version2):
            v1, i = check(version1, i)
            v2, j = check(version2, j)
            if v1 > v2:
                return 1
            if v2 > v1:
                return -1
        return 0
        