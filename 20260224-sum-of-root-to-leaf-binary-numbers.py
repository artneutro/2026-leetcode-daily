# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        solution = 0
        # BFS to get all values
        bfs_queue = [[root, str(root.val)]]
        while len(bfs_queue) > 0 :
            next_node = bfs_queue.pop(0)
            if next_node[0].left == None \
            and next_node[0].right == None :
                # Sum up every time it reach a leaf
                solution += int('0b'+next_node[1], 2)
            else :
                if next_node[0].left != None :
                    bfs_queue.append([next_node[0].left, next_node[1] + str(next_node[0].left.val)])
                if next_node[0].right != None :
                    bfs_queue.append([next_node[0].right, next_node[1] + str(next_node[0].right.val)])
        return solution
