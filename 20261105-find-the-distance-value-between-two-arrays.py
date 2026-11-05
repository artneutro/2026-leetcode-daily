# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        solution = 0
        index_i = 0
        while index_i < len(arr1) :
            index_j = 0
            while index_j < len(arr2) :
                if abs(arr1[index_i]-arr2[index_j]) <= d :
                    break
                index_j += 1
            if index_j == len(arr2) :
                solution += 1
            index_i += 1
        return solution
        
