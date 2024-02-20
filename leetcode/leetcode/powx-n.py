class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n):
            # print(x, n)
            if n == 0:
                return 1
            if n < 0:
                return 1/rec(x, -n)
            a = rec(x*x, n//2)
            if n%2 != 0:
                return x*a
            return a
    
        return rec(x, n)
        