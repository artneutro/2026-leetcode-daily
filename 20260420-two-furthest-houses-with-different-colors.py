# https://leetcode.com/problems/two-furthest-houses-with-different-colors/
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        solution = 0
        # Store ~ O(n)
        col_ind = {}
        index = 0
        while index < len(colors) :
            if colors[index] in col_ind :
                if len(col_ind[colors[index]]) == 2 :
                    col_ind[colors[index]][-1] = index
                else :
                    col_ind[colors[index]].append(index)
            else :
                col_ind[colors[index]] = [index]
            index += 1
        # Complete ~ O(n)
        values = list(col_ind.values())
        for item in values :
            if len(item) == 1 :
                item.append(item[0])
        # Check ~ O(n**2)
        index_x = 0
        while index_x < len(values) :
            index_y = 0 
            while index_y < len(values) :
                if index_x != index_y \
                and abs(values[index_x][0]-values[index_y][1]) > solution :
                    solution = abs(values[index_x][0]-values[index_y][1])
                index_y += 1
            index_x += 1
        return solution 

