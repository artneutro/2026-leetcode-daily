# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        items_A = {}
        items_B = {}
        found = 0
        C = []
        for i in range(len(A)) :
            if A[i] == B[i] :
                found += 1
            else :
                items_A[A[i]] = 1
                items_B[B[i]] = 1
                if A[i] in items_B :
                    found += 1
                if B[i] in items_A :
                    found += 1
            C.append(found)
        return C
