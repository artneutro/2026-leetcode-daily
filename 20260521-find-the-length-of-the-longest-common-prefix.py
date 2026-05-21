# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_len = 0
        prefix = {}
        # Fill prefix dict with arr1 ~ O(nxm) Size of arr1 x size of max str
        for i in range(len(arr1)) :
            str_1 = str(arr1[i]) 
            while len(str_1) > 0 :
                if str_1 in prefix :
                    break
                else :
                    prefix[str_1] = 1
                str_1 = str_1[:-1]
        # Look for matches with arr2 ~ O(oxp) Size of arr2 x size of max str
        for i in range(len(arr2)) :
            str_2 = str(arr2[i]) 
            while len(str_2) > 0 :
                if str_2 in prefix :
                    if len(str_2) > max_len :
                        max_len = len(str_2)
                    break
                str_2 = str_2[:-1]
        return max_len
