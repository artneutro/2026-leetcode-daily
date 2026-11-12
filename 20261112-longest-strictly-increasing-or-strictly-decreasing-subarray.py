# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        solution = 0
        size = 0
        incr = True
        index = 0
        while index < len(nums)-1 :
            if nums[index] < nums[index+1] and incr :
                size += 1
            elif nums[index] < nums[index+1] and not incr :
                if size > solution :
                    solution = size
                size = 1
                incr = True
            elif nums[index] > nums[index+1] and not incr :
                size += 1
            elif nums[index] > nums[index+1] and incr :
                if size > solution :
                    solution = size
                size = 1
                incr = False
            else :
                if size > solution :
                    solution = size
                size = 0
            index += 1
        if size > solution :
            return size+1
        return solution+1
