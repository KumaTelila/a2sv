class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ''
        for i in digits:
            st +=str(i)
        a = str(int(st)+1)
        ls = []
        for i in a:
            ls.append(int(i))
        return ls