# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            if first < second:
                ele = -first - -second
                heappush(stones, -ele)
        return  -stones[0] if stones else 0
        