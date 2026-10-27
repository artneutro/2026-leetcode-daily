# https://leetcode.com/problems/create-grid-with-exactly-one-path/
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        default_p = ''
        default_h = ''
        for _ in range(n-1) :
            default_p += '.'
            default_h += '#'
        default_p += '.'
        default_h += '.'
        grid.append(default_p)
        for i in range(m-1) :
            grid.append(default_h)
        return grid
        
