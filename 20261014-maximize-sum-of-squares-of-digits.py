# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
class Solution:
    def maxSumOfSquares(self, num: int, suma: int) -> str:
        # Initialize variables
        solution = ''
        ind_val = 9
        cur_sum = 0
        # O(n) => Assign the max possible solution from 9 to 0, e.g. 99988776...
        while cur_sum <= suma and ind_val > 0 and len(solution) < num :
            if cur_sum + ind_val <= suma :
                solution = solution + str(ind_val)
                cur_sum += ind_val
            else :
                ind_val -= 1
        # O(m) => If len reached, check
        if len(solution) == num :
            if sum(int(item) for item in solution) == suma :
                return solution
        # O(m) => If we haven't reached num, then fill with extra zeroes 0 and check
        else :
            while len(solution) < num :
                solution = solution + '0'
            if sum(int(item) for item in solution) == suma :
                return solution
        # No solution found
        return ''
        

