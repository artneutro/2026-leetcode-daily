# https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        solution = ''
        counter = 0
        index = 0
        while index < len(s) :
            if s[index] == '(' :
                counter += 1
                if counter != 1 :
                    solution += s[index]
            else :
                counter -= 1
                if counter != 0 :
                    solution += s[index]
            index += 1
        return solution
