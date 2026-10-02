# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        solution = []
        queue = []
        queue.append([1,0,'('])
        while len(queue) :
            next_path = queue.pop(0)
            # It reached the end
            if len(next_path[2]) == 2*n :
                solution.append(next_path[2])
            # Insert string + '('
            if next_path[0] < n :
                queue.append([next_path[0]+1,next_path[1],next_path[2]+'('])
            # Insert string + ')'
            if next_path[0] > next_path[1] :
                queue.append([next_path[0],next_path[1]+1,next_path[2]+')'])
        return solution
        
