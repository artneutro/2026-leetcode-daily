# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s :
            if i == ')' :
                if len(stack) <= 0 or stack[-1] != '(' :
                    return False
                else :
                    stack.pop(-1)
            elif i == ']' :
                if len(stack) <= 0 or stack[-1] != '[' :
                    return False
                else :
                    stack.pop(-1)
            elif i == '}' :
                if len(stack) <= 0 or stack[-1] != '{' :
                    return False
                else :
                    stack.pop(-1)
            else :
                stack.append(i)
        if len(stack) > 0 :
            return False
        return True
