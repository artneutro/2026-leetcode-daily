# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        solution = 1000
        dic = {}
        # Store ~ O(n)
        index = 0
        while index < len(words) :
            if words[index] in dic :
                dic[words[index]].append(index)
            else :
                dic[words[index]] = [index]
            index += 1
        # Check ~ O(n)
        if target in dic :
            for item in dic[target] :
                option = abs(item-startIndex)
                if option < solution :
                    solution = option
                option = ((len(words)-(max(item,startIndex)))+min(item,startIndex))
                if option < solution :
                    solution = option
        else :
            return -1
        return solution
