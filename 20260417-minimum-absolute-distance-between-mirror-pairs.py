# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        solution = len(nums)
        # key: all numbers, value: last index where this number was found
        items = {}
        # key: all reverses, value: the numbers that generated this reverse
        found = {}
        index = 0
        while index < len(nums) :
            # Check if a reverse was found
            if nums[index] in found :
                item_list = found[nums[index]]
                for elem in item_list :
                    if abs(items[elem]-index) < solution :
                        solution = abs(items[elem]-index)
            # Update last index found for this number
            items[nums[index]] = index
            # Store reverse
            reversed_item = int(str(nums[index])[::-1])
            if reversed_item not in found :
                found[reversed_item] = [nums[index]]
            else :
                # Optimization when many are repeated
                if nums[index] not in found[reversed_item] :
                    found[reversed_item].append(nums[index])
            index += 1
        if solution == len(nums) :
            return -1
        return solution
