class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1 and citations[0] > 0:
            return 1
        if  citations[-1] == 0:
            return 0
        if len(citations)<= citations[0]:
            return len(citations)
        low = 1
        high = len(citations)
        best = 0
        while low <= high:
            mid = low + (high - low)//2
            if mid >= citations[len(citations) - mid - 1]:
                best = mid
                high = mid - 1
            else:
                low = mid  + 1        
        return best
        