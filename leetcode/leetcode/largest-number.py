class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def larger(x, y):
            return x + y > y + x
        st = ''.join(sorted(map(str, nums), key = LargerNumKey))
        return '0' if st[0] == '0' else st
        