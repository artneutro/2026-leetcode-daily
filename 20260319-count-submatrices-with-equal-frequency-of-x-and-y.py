# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        solution = 0
        prefix_s = {}
        xs_found = 1001
        # Prefix sum O(mxn)
        index_y = 0
        while index_y < len(grid[0]) :
            current = 0
            index_x = 0
            while index_x < len(grid) :
                # X ==> +1, Y ==> -1, . ==> +0
                if index_x in prefix_s :
                    if grid[index_x][index_y] == 'X' :
                        prefix_s[index_x] += 1
                        if index_x < xs_found :
                            xs_found = index_x
                    elif grid[index_x][index_y] == 'Y' :
                        prefix_s[index_x] -= 1
                else :
                    if grid[index_x][index_y] == 'X' :
                        prefix_s[index_x] = 1
                        if index_x < xs_found :
                            xs_found = index_x
                    elif grid[index_x][index_y] == 'Y' :
                        prefix_s[index_x] = -1
                    else :
                        prefix_s[index_x] = 0
                # Must be zero
                current += prefix_s[index_x]
                # X must be found before or during current row
                if current == 0 and xs_found <= index_x :
                    solution += 1
                index_x += 1
            index_y += 1
        return solution 
