# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums) :
            if sum(int(x) for x in str(nums[index])) == index :
                return index
            index += 1
        return -1 
