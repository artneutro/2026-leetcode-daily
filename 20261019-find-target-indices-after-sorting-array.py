# https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        s_nums = sorted(nums)
        solution = []
        index = 0
        while index < len(s_nums) :
            if s_nums[index] == target :
                solution.append(index)
            index += 1
        return solution
        
