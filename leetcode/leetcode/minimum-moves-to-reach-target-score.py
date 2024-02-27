class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target-1
        ans = 0
        while target != 1:
            if maxDoubles == 0:
                ans+=target-1
                break
            else:
                if target%2 == 0:
                    target//=2
                    ans+=1
                    maxDoubles-=1
                else:
                    target-=1
                    ans+=1
        return ans
        