# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        solution = 0
        size = 1
        while size <= len(nums) :
            index = 0
            while index+size <= len(nums) :
                solution += len(set(nums[index:index+size]))**2
                index += 1
            size += 1
        return solution
