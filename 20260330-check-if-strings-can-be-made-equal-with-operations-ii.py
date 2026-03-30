# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        eve = {}
        odd = {}
        # Store ~ O(n)
        index = 0
        while index < len(s1) :
            if index%2 == 0 :
                if s1[index] in eve :
                    eve[s1[index]] += 1
                else :
                    eve[s1[index]] = 1
                if s2[index] in eve :
                    eve[s2[index]] -= 1
                else :
                    eve[s2[index]] = -1
            else :
                if s1[index] in odd :
                    odd[s1[index]] += 1
                else :
                    odd[s1[index]] = 1
                if s2[index] in odd :
                    odd[s2[index]] -= 1
                else :
                    odd[s2[index]] = -1
            index += 1
        # Check ~ O(26)
        for item in eve :
            if eve[item] != 0 :
                return False
        for item in odd :
            if odd[item] != 0 :
                return False
        return True
