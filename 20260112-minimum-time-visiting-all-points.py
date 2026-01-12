# https://leetcode.com/problems/minimum-time-visiting-all-points/
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        curr_point = points.pop(0)
        while len(points) > 0 :
            next_point = points.pop(0)
            # Go diagonal until reach same x or y
            while curr_point[0] != next_point[0] and curr_point[1] != next_point[1] :
                if curr_point[0] > next_point[0] :
                    curr_point[0] -= 1
                else :
                    curr_point[0] += 1
                if curr_point[1] > next_point[1] :
                    curr_point[1] -= 1
                else :
                    curr_point[1] += 1
                time += 1
            # Add the remaining 
            if curr_point[0] == next_point[0] :
                time += max(curr_point[1],next_point[1])-min(curr_point[1],next_point[1])
            else :
                time += max(curr_point[0],next_point[0])-min(curr_point[0],next_point[0])
            curr_point[0] = next_point[0]
            curr_point[1] = next_point[1]
        return time
