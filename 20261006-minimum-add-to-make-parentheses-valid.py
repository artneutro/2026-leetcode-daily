# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        solution = 0
        stack = 0
        index = 0
        while index < len(s) :
            if s[index] == '(' :
                stack += 1
            else :
                if stack == 0 :
                    solution += 1
                else :
                    stack -= 1
            index += 1
        solution += stack
        return solution
