# https://leetcode.com/problems/equal-sum-grid-partition-i/
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Populate O(mxn)
        rows = {}
        cols = {}
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if i in rows :
                    rows[i] += grid[i][j] 
                else :
                    rows[i] = grid[i][j] 
                if j in cols :
                    cols[j] += grid[i][j] 
                else :
                    cols[j] = grid[i][j] 
        # Check O(m+n)
        rows = list(rows.values())
        sum_rows = sum(rows)
        chk_rows = 0
        index = 0
        while index < len(rows) :
            chk_rows += rows[index] 
            if 2*chk_rows == sum_rows :
                return True
            index += 1
        cols = list(cols.values())
        sum_cols = sum(cols)
        chk_cols = 0
        index = 0
        while index < len(cols) :
            chk_cols += cols[index] 
            if 2*chk_cols == sum_cols :
                return True
            index += 1
        return False
