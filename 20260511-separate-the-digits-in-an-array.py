# https://leetcode.com/problems/separate-the-digits-in-an-array/
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        solution = []
        for item in nums :
            for elem in str(item) :
                solution.append(int(elem))
        return solution
        
