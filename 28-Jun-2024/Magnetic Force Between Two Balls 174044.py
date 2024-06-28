# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(mid):
            count = 1
            prevind = 0
            for i in range(1, len(position)):
                if position[i] - position[prevind] >= mid:
                    count += 1
                    prevind = i
            return count >= m
        # if m == 2:
        #     return position[-1] - position[0]
        ans = -1
        l = 0
        r = max(position) 

        while l <= r:
            mid = (r + l)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans
        