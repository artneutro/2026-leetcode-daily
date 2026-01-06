# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_total = {}
        # BFS
        nodes_queue = []
        nodes_queue.append((root, 1))
        while len(nodes_queue) > 0 :
            next_node = nodes_queue.pop(0)
            if next_node[1] in level_total :
                level_total[next_node[1]] += next_node[0].val
            else :
                level_total[next_node[1]] = next_node[0].val
            if next_node[0].left != None :
                nodes_queue.append((next_node[0].left, next_node[1]+1))
            if next_node[0].right != None :
                nodes_queue.append((next_node[0].right, next_node[1]+1))
        # Check maximal
        max_sum = root.val
        max_lev = 1
        for key,val in level_total.items() :
            if val > max_sum :
                max_sum = val
                max_lev = key
        return max_lev
