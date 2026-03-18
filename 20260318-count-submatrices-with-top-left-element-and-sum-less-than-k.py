# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        solution = 0
        sum_up_t = {}
        # Iterate and memorize past sums O(mxn)
        index_y = 0
        while index_y < len(grid[0]) :
            col_sum = 0 
            index_x = 0
            while index_x < len(grid) :
                if index_x in sum_up_t :
                    sum_up_t[index_x] += grid[index_x][index_y]
                else :
                    sum_up_t[index_x] = grid[index_x][index_y]
                col_sum += sum_up_t[index_x]
                if col_sum <= k :
                    solution += 1
                index_x += 1
            index_y += 1
        return solution
