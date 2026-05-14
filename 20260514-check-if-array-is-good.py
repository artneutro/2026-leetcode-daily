# https://leetcode.com/problems/check-if-array-is-good/
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        if len(sorted_nums) < 2 \
        or (sorted_nums[-1] != sorted_nums[-2]) \
        or (sorted_nums[0] != 1) \
        or (sorted_nums[-1] != len(sorted_nums)-1) :
            return False
        for i in range(len(nums)-2) :
            if sorted_nums[i] != i+1 :
                return False
        return True
