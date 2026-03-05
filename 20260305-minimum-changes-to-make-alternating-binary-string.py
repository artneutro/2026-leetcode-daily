# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
class Solution:
    def minOperations(self, s: str) -> int:
        # Base cases
        if s == '0'*len(s) \
        or s == '1'*len(s) :
            return int(len(s)/2)
        # Otherwise
        s_1 = 0
        s_2 = 0
        s_tmp = True
        # O(n)
        index = 0
        while index < len(s)-2 :
            while s[index] != s[index+1] \
            and index < len(s)-2 :
                if s_tmp :
                    s_1 += 1
                else :
                    s_2 += 1
                index += 1
            # 
            if index < len(s)-2 :
                if s_tmp :
                    s_1 += 1
                else :
                    s_2 += 1
                s_tmp = (not s_tmp)
                index += 1
        # O(1)
        if s[index] != s[index+1] :
            if s_tmp :
                s_1 += 2
            else :
                s_2 += 2
        else :
            s_1 += 1
            s_2 += 1
        # O(1)
        return min(s_1, s_2)

  
