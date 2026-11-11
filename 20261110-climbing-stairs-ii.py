# https://leetcode.com/problems/climbing-stairs-ii/
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        min_costs = {0: 0}
        # O(n)
        iterator = 0
        while iterator < n :
            for index in range(iterator, iterator+3) :
                if index < n :
                    formula = (min_costs[iterator] + costs[index] + (((index+1) - iterator)**2))
                    if index+1 in min_costs :
                        if formula < min_costs[index+1] :
                            min_costs[index+1] = formula
                    else :
                        min_costs[index+1] = formula
            iterator += 1
        return min_costs[n]
