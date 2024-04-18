# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapify(piles)
        while k > 0:
            ele = heappop(piles)
            heappush(piles, ele//2)
            k-=1
        return -sum(piles)
        