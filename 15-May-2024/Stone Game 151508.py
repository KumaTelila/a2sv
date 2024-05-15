# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(i, j, player = True):
            if i == j:
                return True
            alice  = 0
            bob = 0
            if (i, j, player) in memo:
                return memo[(i, j, player)]
            if player:
                alice = max(piles[i] + dp(i+1, j, False), piles[j] + dp(i, j-1, False))
            else:
                bob = max(piles[i] + dp(i+1, j, True), piles[j] + dp(i, j-1, True))
            memo[(i, j, player)] =  alice > bob
            return memo[(i, j, player)]

        ans = dp(0, len(piles) - 1, True)
        return ans


        