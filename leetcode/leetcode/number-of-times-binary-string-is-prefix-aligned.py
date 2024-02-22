class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        _max = -float('inf')
        count = 0
        ans = 0
        for i in flips:
            if count == _max:
                ans+=1
            _max = max(i, _max)
            count+=1
        if count == _max:
            ans+=1
        return ans
            

            

        