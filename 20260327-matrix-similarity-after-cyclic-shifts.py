# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        index = 0
        while index < len(mat) :
            if index%2 == 0 :
                if mat[index] != mat[index][k:]+mat[index][:k] :
                    return False
            else :
                if mat[index] != mat[index][-k:]+mat[index][:-k] :
                    return False
            index += 1
        return True
