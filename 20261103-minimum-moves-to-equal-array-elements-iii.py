# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        solution = 0
        max_nums = max(nums)
        for item in nums :
            if item != max_nums :
                solution += max_nums-item
        return solution
      
