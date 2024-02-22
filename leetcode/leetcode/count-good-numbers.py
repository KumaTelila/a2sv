class Solution:
    ans = 1
    def countGoodNumbers(self, n: int) -> int:
        mdl = 10**9 + 7
        power = n//2
        four = pow(4, power, mdl)
        five = pow(5, power, mdl)
        if n%2 != 0:
            five*=5%mdl
        return (four*five)%mdl
            
        