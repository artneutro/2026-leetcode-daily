# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # O(n)
        index = 0
        while index < len(s) :
            if s[index] == '0' :
                break
            index += 1
        if index < len(s) :
            while index < len(s) :
                if s[index] == '1' :
                    return False
                index += 1
        return True
