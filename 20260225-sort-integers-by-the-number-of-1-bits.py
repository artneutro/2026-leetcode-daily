# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n_ones = {}
        index = 0
        while index < len(arr) :
            bin_rep_ones = str(bin(arr[index]))[2:].count('1')
            if bin_rep_ones in n_ones :
                n_ones[bin_rep_ones].append(arr[index])
            else :
                n_ones[bin_rep_ones] = [arr[index]]
            index += 1
        solution = []
        for item in sorted(n_ones) :
            for elem in sorted(n_ones[item]) :
                solution.append(elem)
        return solution
