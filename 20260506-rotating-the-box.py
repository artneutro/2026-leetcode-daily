# https://leetcode.com/problems/rotating-the-box/
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # Create grid nxm
        solution = [([0]*len(boxGrid)) for i in range(len(boxGrid[0]))]
        # Fill copy
        for i in range(len(boxGrid)) :
            for j in range(len(boxGrid[0])) :
                solution[j][len(boxGrid)-1-i] = boxGrid[i][j]
        # Iterate per column using y and floor pointers
        for x in range(len(solution[0])) :
            floor = len(solution)-1
            y = len(solution)-1
            while y >= 0 :
                # Find next floor (empty pos)
                while y >= 0 and solution[y][x] != '.' :
                    y -= 1
                if y < 0 :
                    break
                else :
                    floor = y
                # Find next ceili (stone pos) 
                while y >= 0 :
                    if solution[y][x] == '*' :
                        # If obstacle, update floor
                        while y >= 0 and solution[y][x] != '.' :
                            y -= 1
                        if y < 0 :
                            break
                        else :
                            floor = y
                    elif solution[y][x] == '#' :
                        solution[y][x] = '.'
                        solution[floor][x] = '#'
                        # If stone, update floor
                        while floor >= 0 and solution[floor][x] != '.' :
                            floor -= 1
                        if floor < 0 :
                            break
                        else :
                            if y > floor :
                                y = floor
                    y -= 1
        return solution
