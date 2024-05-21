# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # def dp(ind):
        #     # print(ind)
        #     if ind >= len(arr):
        #         return 0
        #     take = 0
        #     for i in range(ind - 1, -1, -1):
        #         if arr[i] + difference == arr[ind]:
        #             take +=  1
        #     return take
        #     # return 0
            
        # ans = 0
        # for i in range(1, len(arr)):
        #     ans = max(ans, dp(i))
        #     print(i, dp(i))
        # ans = dp(1)
        dp = defaultdict(int)
        for i in range(len(arr)):
            dp[arr[i]] = dp[arr[i] - difference] + 1
        return max(dp.values())
            