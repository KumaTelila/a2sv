# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        original = heights.copy()
        heights.sort()
        ans = 0
        for i in range(len(heights)):
            if original[i] != heights[i]:
                ans += 1

        return ans
        