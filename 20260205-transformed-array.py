# https://leetcode.com/problems/transformed-array/
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        index = 0
        while index < len(nums) :
            if nums[index] > 0 :
                if index+nums[index] < len(nums) :
                    result.append(nums[index+nums[index]])
                else :
                    factor = nums[index]%len(nums)
                    if index+factor < len(nums) :
                        result.append(nums[index+factor])
                    else :
                        result.append(nums[abs(len(nums)-(index+factor))])
            elif nums[index] < 0 : 
                if index-abs(nums[index]) >= 0 :
                    result.append(nums[index-abs(nums[index])])
                else :
                    factor = abs(nums[index])%len(nums)
                    result.append(nums[index-factor])                  
            else :
                result.append(nums[index])
            index += 1
        return result
