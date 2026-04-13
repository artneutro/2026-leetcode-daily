# https://leetcode.com/problems/minimum-distance-to-the-target-element/
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        solution = 100000
        index = 0
        while index < len(nums) :
            if nums[index] == target :
                if abs(index-start) < solution :
                    solution = abs(index-start)
            index += 1
        return solution
        
