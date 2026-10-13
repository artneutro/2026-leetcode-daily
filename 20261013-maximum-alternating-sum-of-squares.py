# https://leetcode.com/problems/maximum-alternating-sum-of-squares/
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # O(n)
        index = 0
        while index < len(nums) :
            nums[index] = nums[index]**2
            index += 1
        # O(nlogn)
        nums_s = sorted(nums, reverse=True)
        # O(n)
        if len(nums)%2 == 0 :
            return sum(nums_s[:len(nums)//2])-sum(nums_s[len(nums)//2:])
        else :
            return sum(nums_s[:(len(nums)//2)+1])-sum(nums_s[(len(nums)//2)+1:])


