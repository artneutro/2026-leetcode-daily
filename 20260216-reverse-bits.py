# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        bin_rep = (str(bin(n))[2:])
        while len(bin_rep) < 32 :
            bin_rep = '0' + bin_rep
        return int('0b' + bin_rep[::-1], 2)
