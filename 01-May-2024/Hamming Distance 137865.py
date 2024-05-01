# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        l = n.bit_length()
        top = 2**l
        return top - n - 1