# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        index_q = 0
        while index_q < len(queries) :
            index_i = queries[index_q][0]
            while index_i <= queries[index_q][1] :
                nums[index_i] = (nums[index_i]*queries[index_q][3])%(10**9+7)
                index_i += queries[index_q][2]
            index_q += 1
        solution = 0 
        for item in nums :
            solution ^= item
        return solution
