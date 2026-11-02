# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        solution = 0
        max_option = sorted(nums)[len(nums)//2]
        for item in nums :
            if item != max_option :
                solution += abs(item-max_option)
        return solution
