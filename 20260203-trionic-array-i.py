# https://leetcode.com/problems/trionic-array-i/
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        cache = [0, 0, 0]
        index = 0
        while index < len(nums)-1 : 
            if nums[index] > nums[index+1] : 
                if cache[0] == 0 or cache[2] != 0 :
                    return False
                else :
                    cache[1] += 1 
            elif nums[index] < nums[index+1] :
                if cache[1] == 0 :
                    cache[0] += 1
                else :
                    cache[2] += 1 
            else :
                return False
            index += 1
        if index == len(nums)-1 and cache[0] > 0 and cache[1] > 0 and cache[2] > 0 :
            return True
        return False
