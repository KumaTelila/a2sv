# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        sm = 0
        for i in range(1, len(heights)):
            diff = heights[i] -  heights[i-1]
            if diff > 0:
                heappush(heap, -diff)
                sm+=diff
            if sm > bricks:
                if ladders > 0:
                    ele = heappop(heap)
                    ladders-=1
                    sm+=ele
                else:
                    bricks -= diff
                    sm -= diff
            if sm > bricks and ladders == 0:
                return i - 1
        return len(heights) - 1



        