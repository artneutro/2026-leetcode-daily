# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        solution = 0
        # Check min(need1, need2)
        min_need = min(need1, need2)
        # Check min(cost1+cost2, costBoth) x min(need1, need2)
        min_cost = min((cost1+cost2), costBoth)
        # Partial solution
        solution = min_need*min_cost
        # Fill remaining max(need1, need2)-min(need1, need2) with min(costN, costBoth)
        rem_need = 0
        rem_cost = 0
        if need1 < need2 :
            rem_need = need2-need1
            rem_cost = cost2
        else :
            rem_need = need1-need2
            rem_cost = cost1
        solution += min(rem_need*rem_cost, rem_need*costBoth)
        return solution
