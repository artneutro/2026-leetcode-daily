# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        solution = 10000
        storage = {}
        # Store ~ O(n)
        index = 0
        while index < len(nums) :
            if nums[index] in storage :
                storage[nums[index]].append(index)
            else :
                storage[nums[index]] = [index]
            index += 1
        # Check ~ O(n)
        for item in storage :
            indexes = storage[item]
            if len(indexes) >= 3 :
                internal_i = 0
                while internal_i < len(indexes)-2 :
                    if 2*(indexes[internal_i+2]-indexes[internal_i]) < solution :
                        solution = 2*(indexes[internal_i+2]-indexes[internal_i])
                    internal_i += 1
        # Return ~ O(1)
        if solution == 10000 :
            return -1
        return solution
