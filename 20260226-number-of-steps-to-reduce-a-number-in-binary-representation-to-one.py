# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
class Solution:
    def numSteps(self, s: str) -> int:
        solution = 0
        while s != '1' :
            # If the current number is even, you have to divide it by 2.
            if s[-1] == '0' :
                s = s[:-1]
            # If the current number is odd, you have to add 1 to it.
            else :
                s = s[:-1]+'0'
                index = len(s)-2
                while s[index] == '1' :
                    s = s[:index] + '0' + s[index+1:]
                    index -= 1
                if index <= 0 :
                    s = '1' + s[index+1:]
                else :
                    s = s[:index] + '1' + s[index+1:]
            solution += 1
        return solution
