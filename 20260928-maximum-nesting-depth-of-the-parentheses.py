# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:
        solution = 0
        stack = 0
        index = 0
        while index < len(s):
            if s[index] == '(' :
                stack += 1
                if stack > solution :
                    solution = stack
            elif s[index] == ')' :
                stack -= 1
            index += 1
        return solution
