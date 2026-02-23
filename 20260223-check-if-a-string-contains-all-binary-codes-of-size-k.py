# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        found = set()
        # Iterate over the string to get all substrings of lenght k ~ O(n-k)
        index = 0
        while index < len(s)-k+1 :
            # Store the substring (as int) in a set ~ O(1)
            found.add(int('0b'+s[index:index+k], 2))
            index += 1
        # Check if all numbers from 0 up to 2**k are in the set ~ O(1)
        if len(found) != 2**k :
            return False
        return True
        
