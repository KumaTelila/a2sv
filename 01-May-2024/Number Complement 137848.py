# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        l = num.bit_length()
        top = 2**l
        return  top - num -1 

        