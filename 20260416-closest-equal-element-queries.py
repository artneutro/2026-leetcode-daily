# https://leetcode.com/problems/closest-equal-element-queries/
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        solution = []
        # Base case
        if sum(nums) == len(nums) :
            return [1]*len(nums)
        # Store ~ O(n)
        ind_hash = {}
        index = 0
        while index < len(nums) :
            if nums[index] in ind_hash :
                ind_hash[nums[index]].append(index)
            else :
                ind_hash[nums[index]] = [index]
            index += 1
        # Check ~ O(mxn)
        index = 0
        while index < len(queries) :
            if len(ind_hash[nums[queries[index]]]) == 1 :
                solution.append(-1)
            else :
                lookup_index = 0
                while ind_hash[nums[queries[index]]][lookup_index] != queries[index] :
                    lookup_index += 1
                # lookup_index contains current position of current queried index in ind_hash
                if lookup_index == 0 :
                    part1 = ind_hash[nums[queries[index]]][lookup_index+1]-ind_hash[nums[queries[index]]][lookup_index]
                    part2 = (len(nums)-ind_hash[nums[queries[index]]][-1])+ind_hash[nums[queries[index]]][lookup_index]
                    solution.append(min(part1, part2))
                elif lookup_index == len(ind_hash[nums[queries[index]]])-1 :
                    part1 = ind_hash[nums[queries[index]]][lookup_index]-ind_hash[nums[queries[index]]][lookup_index-1]
                    part2 = len(nums)-ind_hash[nums[queries[index]]][-1]+ind_hash[nums[queries[index]]][0]
                    solution.append(min(part1, part2))
                else :
                    part1 = ind_hash[nums[queries[index]]][lookup_index+1]-ind_hash[nums[queries[index]]][lookup_index]
                    part2 = ind_hash[nums[queries[index]]][lookup_index]-ind_hash[nums[queries[index]]][lookup_index-1]
                    solution.append(min(part1, part2))
            index += 1
        return solution
      
