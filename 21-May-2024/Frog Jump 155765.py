# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        st = set(stones)
        @cache
        def dp(unit, prev):
            if unit == stones[-1]:
                return True
            if unit not in st or prev == 0:
                return False
            flag = False
            if unit == 0:
                return dp(unit+1,prev)
            for i in (-1, 0, 1):
                flag = flag or dp(prev + unit + i, prev + i)
            return flag
        ans = dp(0, 1)
        return ans
    