# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # n = len(questions)
        # dp = [0]*len(questions)
        # for i in range(len(questions)):
        #     point = questions[i][0]
        #     brain = questions[i][1]
        #     dp[i] += point
        #     nxt = i + brain + 1
        #     if nxt < n:
        #         dp[nxt] += point
        # print(dp)
        # return max(dp)

        # top down
        n = len(questions)
        memo = {}
        def dp(ind):
            if ind >= n:
                return 0
            if ind in memo:
                return memo[ind]
            take = dp(ind + 1 + questions[ind][1]) + questions[ind][0]
            nottake = dp(ind + 1)
            memo[ind] =  max(take, nottake)
            return memo[ind]
        return dp(0)
