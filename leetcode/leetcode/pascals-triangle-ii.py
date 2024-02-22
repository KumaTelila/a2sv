class Solution:
    # ans = [1]
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        def rec(n, i):
            if i > n:
                return ans
            val = ans[-1] * (n - i + 1)//i
            ans.append(val)  
            return rec(n, i+1)
        return rec(rowIndex, 1)


        