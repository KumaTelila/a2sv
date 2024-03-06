class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        n = len(piles)
        best = high
        while low <= high:
            mid = low + (high - low)//2
            hours = 0
            for i in range(n):
                hours +=ceil(piles[i]/mid)
            if hours <= h:
                best =  mid
                high = mid - 1
            else:
                low = mid + 1
        return best
                    
        