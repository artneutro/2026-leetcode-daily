# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        solution = []
        # Store hashmap ~ O(nxm) where n is len of words and m len of dictionary
        for q_item in queries :
            for d_item in dictionary :
                count = 0
                for index in range(len(d_item)) :
                    if q_item[index] != d_item[index] :
                        count += 1
                    if count > 2 :
                        break
                if count <= 2 :
                    solution.append(q_item)
                    break
        return solution 
