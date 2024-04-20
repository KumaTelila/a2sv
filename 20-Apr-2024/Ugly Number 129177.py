# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        d = 2
        while d*d <= n:
            while n%d == 0:
                n//=d
            d+=1
            if d >= 7:
                return False
        if n >= 7:
            return False
        return True
        