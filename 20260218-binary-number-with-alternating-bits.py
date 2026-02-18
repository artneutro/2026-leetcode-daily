# https://leetcode.com/problems/binary-number-with-alternating-bits/
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = str(bin(n))[2:]
        init = bin_n[0] 
        index = 1 
        while index < len(bin_n) : 
            if init == '0' :
                if bin_n[index] != '1' :
                    return False
                else :
                    init = '1'
            else :
                if bin_n[index] != '0' :
                    return False
                else :
                    init = '0'
            index += 1
        return True
