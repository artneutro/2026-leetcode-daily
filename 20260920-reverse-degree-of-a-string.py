# https://leetcode.com/problems/reverse-degree-of-a-string/
class Solution:
    def reverseDegree(self, s: str) -> int:
        ascii_list = list(string.ascii_lowercase)
        ascii_hash = {}
        n = 0
        for item in ascii_list :
            ascii_hash[item] = len(ascii_list)-n
            n += 1
        solution = 0
        index = 0
        while index < len(s) :
            solution += ascii_hash[s[index]]*(index+1)
            index += 1
        return solution
