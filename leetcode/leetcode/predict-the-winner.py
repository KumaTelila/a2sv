class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(start, end, p1, p2, turn = True):
            if start > end:
                return p1 >= p2
            if turn:
                return winner(start+1, end, p1+nums[start], p2, not turn) \
                or winner(start, end-1, p1+nums[end], p2, not turn)
            else:
                return winner(start+1, end, p1, p2+nums[start], not turn) \
                and winner(start, end-1, p1, p2+nums[end], not turn)  
        return winner(0, len(nums) - 1, 0, 0, True)
        