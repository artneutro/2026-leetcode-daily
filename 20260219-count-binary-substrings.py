# https://leetcode.com/problems/count-binary-substrings/
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        solution = 0
        current = s[0]
        zeroes = 0
        ones = 0
        # Base case
        if current == '0' :
            zeroes += 1
        else :
            ones += 1
        # Rest
        index = 1
        while index < len(s) :
            if (s[index] == '0' and current == '1'):
                solution += min(zeroes, ones)
                current = '0'
                zeroes = 1
            elif (s[index] == '0' and current == '0'):
                zeroes += 1
            elif (s[index] == '1' and current == '0'):
                solution += min(zeroes, ones)
                current = '1'
                ones = 1
            elif (s[index] == '1' and current == '1'):
                ones += 1
            index += 1
        solution += min(zeroes, ones)
        return solution
