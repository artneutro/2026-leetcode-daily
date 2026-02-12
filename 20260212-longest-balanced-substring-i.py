# https://leetcode.com/problems/longest-balanced-substring-i/
class Solution:
    def longestBalanced(self, s: str) -> int:
        solution = 0
        index = 0
        while index < len(s) :
            found_alpha = {}
            internal_index = index
            while internal_index < len(s) :
                if s[internal_index] not in found_alpha :
                    found_alpha[s[internal_index]] = 1
                else :
                    found_alpha[s[internal_index]] += 1
                # Check if new solution was found
                if len(set(found_alpha.values())) == 1 :
                    suma = sum(list(found_alpha.values()))
                    if suma > solution :
                        solution = suma
                internal_index += 1
            index += 1
        return solution
