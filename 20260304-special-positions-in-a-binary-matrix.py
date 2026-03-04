# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        solution = 0
        # O(mxn)
        rows = {}
        cols = {}
        for i in range(len(mat)) :
            for j in range(len(mat[0])) :
                if mat[i][j] == 1 :
                    if i in rows :
                        rows[i].append(j)
                    else :
                        rows[i] = [j]
                    if j in cols :
                        cols[j].append(i)
                    else :
                        cols[j] = [i]
        # O(m)
        for item in rows :
            if len(rows[item]) == 1 :
                if len(cols[rows[item][0]]) == 1 \
                and cols[rows[item][0]][0] == item :
                    solution += 1
        return solution
