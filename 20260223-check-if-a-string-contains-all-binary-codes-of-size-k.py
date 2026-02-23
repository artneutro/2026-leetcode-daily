# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        found = set()
        # Iterate over the string to get all substrings of lenght k
        index = 0
        while index < len(s)-k+1 :
        # Store the substring in a set
            found.add(int('0b'+s[index:index+k], 2))
            index += 1
        # Check if all numbers from 0 up to 2**k are in the set
        for i in range(2**k) :
            if i not in found :
                return False
        return True
